#!/usr/bin/env python3
"""Simulación integral de la Unidad 3: modulación digital con impairments.

Implementa una cadena Tx-CH-Rx en pasabanda con:
- Modulación Gray: BPSK, QPSK, 8-PSK, 16-QAM, 64-QAM.
- Conformación de pulsos RRC.
- Canal AWGN, Rayleigh y Rician.
- Impairments: CFO, offset de fase, desbalance I/Q y combinados.
- Demapper duro y blando (LLR exacto y max-log).
- Curvas BER y visualizaciones guardadas en figuras/.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import hilbert
from scipy.special import erfc, i0, logsumexp


# -----------------------------------------------------------------------------
# Utilidades matemáticas y configuraciones de modulación
# -----------------------------------------------------------------------------


def qfunc(x: np.ndarray | float) -> np.ndarray | float:
    """Función Q usando erfc para estabilidad numérica."""
    return 0.5 * erfc(np.asarray(x) / np.sqrt(2.0))


@dataclass
class ModulationConfig:
    nombre: str
    M: int
    bits_por_simbolo: int
    tipo: str
    constelacion: np.ndarray
    etiquetas_bits: np.ndarray
    mapa_bits_a_indice: Dict[Tuple[int, ...], int]


def int_to_bits_vector(valores: np.ndarray, nbits: int) -> np.ndarray:
    """Convierte enteros a vectores de bits MSB->LSB."""
    valores = np.asarray(valores, dtype=int)
    shifts = np.arange(nbits - 1, -1, -1)
    return ((valores[:, None] >> shifts) & 1).astype(int)


def bits_to_int_vector(bits: np.ndarray) -> np.ndarray:
    """Convierte filas de bits MSB->LSB a enteros."""
    bits = np.asarray(bits, dtype=int)
    pesos = 1 << np.arange(bits.shape[1] - 1, -1, -1)
    return bits @ pesos


def gray_code(n: np.ndarray | int) -> np.ndarray | int:
    return np.asarray(n) ^ (np.asarray(n) >> 1)


def inverse_gray_scalar(g: int) -> int:
    """Invierte código Gray de forma escalar."""
    x = g
    while g > 0:
        g >>= 1
        x ^= g
    return x


def niveles_gray_pam(m_axis: int) -> Tuple[np.ndarray, np.ndarray]:
    """Niveles PAM en orden +máximo a -máximo con etiquetas Gray adyacentes."""
    bits_axis = int(np.log2(m_axis))
    niveles = np.arange(m_axis - 1, -(m_axis), -2, dtype=float)
    grays = gray_code(np.arange(m_axis))
    etiquetas = int_to_bits_vector(np.asarray(grays, dtype=int), bits_axis)
    return niveles, etiquetas


def crear_bpsk() -> ModulationConfig:
    const = np.array([1.0 + 0j, -1.0 + 0j])
    bits = np.array([[0], [1]], dtype=int)
    mapa = {tuple(b): i for i, b in enumerate(bits)}
    return ModulationConfig("BPSK", 2, 1, "psk", const, bits, mapa)


def crear_qpsk() -> ModulationConfig:
    niveles = np.array([1.0, -1.0])
    bits_axis = np.array([[0], [1]], dtype=int)
    constelacion = []
    etiquetas = []
    for i_i, bi in enumerate(bits_axis):
        for i_q, bq in enumerate(bits_axis):
            constelacion.append(niveles[i_i] + 1j * niveles[i_q])
            etiquetas.append(np.concatenate([bi, bq]))
    const = np.asarray(constelacion, dtype=complex) / np.sqrt(2.0)
    bits = np.asarray(etiquetas, dtype=int)
    mapa = {tuple(b): i for i, b in enumerate(bits)}
    return ModulationConfig("QPSK", 4, 2, "psk", const, bits, mapa)


def crear_mpsk(M: int) -> ModulationConfig:
    k = int(np.log2(M))
    fases = 2.0 * np.pi * np.arange(M) / M
    etiquetas = int_to_bits_vector(np.asarray(gray_code(np.arange(M)), dtype=int), k)
    const = np.exp(1j * fases)
    mapa = {tuple(b): i for i, b in enumerate(etiquetas)}
    return ModulationConfig(f"{M}-PSK", M, k, "psk", const, etiquetas, mapa)


def crear_mqam(M: int) -> ModulationConfig:
    raiz = int(np.sqrt(M))
    if raiz * raiz != M:
        raise ValueError("M debe ser cuadrado perfecto para QAM.")
    bits_axis = int(np.log2(raiz))
    niveles, etiquetas_axis = niveles_gray_pam(raiz)
    constelacion = []
    etiquetas = []
    for i_i, bi in enumerate(etiquetas_axis):
        for i_q, bq in enumerate(etiquetas_axis):
            constelacion.append(niveles[i_i] + 1j * niveles[i_q])
            etiquetas.append(np.concatenate([bi, bq]))
    const = np.asarray(constelacion, dtype=complex)
    const /= np.sqrt(np.mean(np.abs(const) ** 2))
    bits = np.asarray(etiquetas, dtype=int)
    mapa = {tuple(b): i for i, b in enumerate(bits)}
    return ModulationConfig(f"{M}-QAM", M, int(np.log2(M)), "qam", const, bits, mapa)


def obtener_modulaciones() -> Dict[str, ModulationConfig]:
    modulaciones = {
        "BPSK": crear_bpsk(),
        "QPSK": crear_qpsk(),
        "8PSK": crear_mpsk(8),
        "16QAM": crear_mqam(16),
        "64QAM": crear_mqam(64),
    }
    return modulaciones


# -----------------------------------------------------------------------------
# Filtro RRC y cadena Tx/Rx en pasabanda
# -----------------------------------------------------------------------------


def rrc_filter(beta: float, span: int, sps: int) -> np.ndarray:
    """Genera un filtro root-raised-cosine de energía unitaria."""
    t = np.arange(-span * sps / 2, span * sps / 2 + 1, dtype=float) / sps
    h = np.zeros_like(t)

    for idx, tau in enumerate(t):
        if np.isclose(tau, 0.0):
            h[idx] = 1.0 + beta * (4.0 / np.pi - 1.0)
        elif beta > 0 and np.isclose(abs(tau), 1.0 / (4.0 * beta)):
            h[idx] = (
                beta
                / np.sqrt(2.0)
                * (
                    (1.0 + 2.0 / np.pi) * np.sin(np.pi / (4.0 * beta))
                    + (1.0 - 2.0 / np.pi) * np.cos(np.pi / (4.0 * beta))
                )
            )
        else:
            numerador = (
                np.sin(np.pi * tau * (1.0 - beta))
                + 4.0 * beta * tau * np.cos(np.pi * tau * (1.0 + beta))
            )
            denominador = np.pi * tau * (1.0 - (4.0 * beta * tau) ** 2)
            h[idx] = numerador / denominador

    h /= np.sqrt(np.sum(h**2))
    return h


def upsample_symbols(simbolos: np.ndarray, sps: int) -> np.ndarray:
    x = np.zeros(len(simbolos) * sps, dtype=complex)
    x[::sps] = simbolos
    return x


def tx_pulse_shaping(simbolos: np.ndarray, h_rrc: np.ndarray, sps: int) -> np.ndarray:
    return np.convolve(upsample_symbols(simbolos, sps), h_rrc, mode="full")


def upconvert_to_passband(x_bb: np.ndarray, fc_hz: float, fs_hz: float) -> np.ndarray:
    n = np.arange(len(x_bb))
    t = n / fs_hz
    return np.real(x_bb * np.exp(1j * 2.0 * np.pi * fc_hz * t))


def downconvert_from_passband(x_rf: np.ndarray, fc_hz: float, fs_hz: float) -> np.ndarray:
    n = np.arange(len(x_rf))
    t = n / fs_hz
    analitica = hilbert(x_rf)
    return analitica * np.exp(-1j * 2.0 * np.pi * fc_hz * t)


def matched_filter_and_sample(
    x_bb_rx: np.ndarray,
    h_rrc: np.ndarray,
    sps: int,
    n_sym: int,
) -> np.ndarray:
    y = np.convolve(x_bb_rx, h_rrc, mode="full")
    delay = len(h_rrc) - 1
    muestras = y[delay : delay + n_sym * sps : sps]
    return muestras


def coeficientes_iq_imbalance(epsilon: float, phi_iq_rad: float) -> Tuple[complex, complex]:
    alpha = 0.5 * (
        (1.0 + epsilon) * np.exp(-1j * phi_iq_rad / 2.0)
        + (1.0 - epsilon) * np.exp(1j * phi_iq_rad / 2.0)
    )
    beta = 0.5 * (
        (1.0 + epsilon) * np.exp(1j * phi_iq_rad / 2.0)
        - (1.0 - epsilon) * np.exp(-1j * phi_iq_rad / 2.0)
    )
    return alpha, beta


def apply_iq_imbalance(x: np.ndarray, epsilon: float, phi_iq_rad: float) -> np.ndarray:
    alpha, beta = coeficientes_iq_imbalance(epsilon, phi_iq_rad)
    return alpha * x + beta * np.conj(x)


def apply_impairments(
    x: np.ndarray,
    fs_hz: float,
    cfo_hz: float = 0.0,
    phase_offset_rad: float = 0.0,
    iq_epsilon: float = 0.0,
    iq_phase_rad: float = 0.0,
) -> np.ndarray:
    n = np.arange(len(x))
    t = n / fs_hz
    y = x * np.exp(1j * (2.0 * np.pi * cfo_hz * t + phase_offset_rad))
    if abs(iq_epsilon) > 0 or abs(iq_phase_rad) > 0:
        y = apply_iq_imbalance(y, iq_epsilon, iq_phase_rad)
    return y


def generar_ganancia_canal(tipo: str, n_frames: int, rng: np.random.Generator, K: float = 6.0) -> np.ndarray:
    if tipo.lower() == "awgn":
        return np.ones(n_frames, dtype=complex)
    if tipo.lower() == "rayleigh":
        return (rng.normal(size=n_frames) + 1j * rng.normal(size=n_frames)) / np.sqrt(2.0)
    if tipo.lower() == "rician":
        los = np.sqrt(K / (K + 1.0))
        scatter = (rng.normal(size=n_frames) + 1j * rng.normal(size=n_frames)) / np.sqrt(2.0 * (K + 1.0))
        return los + scatter
    raise ValueError(f"Canal no soportado: {tipo}")


def noise_variance_from_ebn0(cfg: ModulationConfig, ebn0_db: float) -> float:
    ebn0 = 10.0 ** (ebn0_db / 10.0)
    return 1.0 / (cfg.bits_por_simbolo * ebn0)


def map_bits_to_symbols(bits: np.ndarray, cfg: ModulationConfig) -> np.ndarray:
    bits = np.asarray(bits, dtype=int)
    k = cfg.bits_por_simbolo
    if len(bits) % k != 0:
        raise ValueError("La longitud de bits debe ser múltiplo de bits_por_simbolo.")
    bloques = bits.reshape(-1, k)
    simbolos = np.empty(len(bloques), dtype=complex)
    for idx, bloque in enumerate(bloques):
        simbolos[idx] = cfg.constelacion[cfg.mapa_bits_a_indice[tuple(bloque.tolist())]]
    return simbolos


def nearest_indices(simbolos_rx: np.ndarray, constelacion: np.ndarray, chunk: int = 20000) -> np.ndarray:
    indices = np.empty(len(simbolos_rx), dtype=int)
    for ini in range(0, len(simbolos_rx), chunk):
        fin = min(ini + chunk, len(simbolos_rx))
        d2 = np.abs(simbolos_rx[ini:fin, None] - constelacion[None, :]) ** 2
        indices[ini:fin] = np.argmin(d2, axis=1)
    return indices


def hard_demapper(simbolos_rx: np.ndarray, cfg: ModulationConfig) -> np.ndarray:
    idx = nearest_indices(simbolos_rx, cfg.constelacion)
    return cfg.etiquetas_bits[idx].reshape(-1)


def cadena_tx_ch_rx(
    bits_tx: np.ndarray,
    cfg: ModulationConfig,
    h_rrc: np.ndarray,
    sps: int,
    rs_hz: float,
    fc_hz: float,
    canal: str,
    ebn0_db: float,
    rng: np.random.Generator,
    cfo_hz: float = 0.0,
    phase_offset_rad: float = 0.0,
    iq_epsilon: float = 0.0,
    iq_phase_rad: float = 0.0,
    K_rician: float = 6.0,
) -> Dict[str, np.ndarray | complex | float]:
    """Cadena completa Bits→Tx→Canal→Rx usando representación RF real."""
    fs_hz = rs_hz * sps
    simbolos_tx = map_bits_to_symbols(bits_tx, cfg)
    x_tx = tx_pulse_shaping(simbolos_tx, h_rrc, sps)

    h_canal = generar_ganancia_canal(canal, 1, rng, K=K_rician)[0]
    x_ch = h_canal * x_tx

    x_imp = apply_impairments(
        x_ch,
        fs_hz=fs_hz,
        cfo_hz=cfo_hz,
        phase_offset_rad=phase_offset_rad,
        iq_epsilon=iq_epsilon,
        iq_phase_rad=iq_phase_rad,
    )

    n0 = noise_variance_from_ebn0(cfg, ebn0_db)
    ruido_bb = np.sqrt(n0 / 2.0) * (
        rng.normal(size=len(x_imp)) + 1j * rng.normal(size=len(x_imp))
    )
    x_rx_bb_equiv = x_imp + ruido_bb

    x_rf = upconvert_to_passband(x_rx_bb_equiv, fc_hz=fc_hz, fs_hz=fs_hz)
    x_rx_bb = downconvert_from_passband(x_rf, fc_hz=fc_hz, fs_hz=fs_hz)
    muestras = matched_filter_and_sample(x_rx_bb, h_rrc, sps, len(simbolos_tx))

    if abs(h_canal) > 1e-12:
        muestras_eq = muestras / h_canal
    else:
        muestras_eq = muestras

    return {
        "bits_tx": bits_tx,
        "simbolos_tx": simbolos_tx,
        "tx_bb": x_tx,
        "canal_h": h_canal,
        "rx_bb_pre_mf": x_rx_bb,
        "rf": x_rf,
        "muestras_rx": muestras,
        "muestras_eq": muestras_eq,
        "n0": n0,
        "fs_hz": fs_hz,
    }


# -----------------------------------------------------------------------------
# LLRs exactos y max-log
# -----------------------------------------------------------------------------


def llr_generico_exacto(simbolos_rx: np.ndarray, cfg: ModulationConfig, n0: float) -> np.ndarray:
    llrs = np.zeros((len(simbolos_rx), cfg.bits_por_simbolo))
    d2 = np.abs(simbolos_rx[:, None] - cfg.constelacion[None, :]) ** 2
    metrica = -d2 / n0
    for b in range(cfg.bits_por_simbolo):
        idx0 = cfg.etiquetas_bits[:, b] == 0
        idx1 = ~idx0
        llrs[:, b] = logsumexp(metrica[:, idx0], axis=1) - logsumexp(metrica[:, idx1], axis=1)
    return llrs


def llr_generico_maxlog(simbolos_rx: np.ndarray, cfg: ModulationConfig, n0: float) -> np.ndarray:
    llrs = np.zeros((len(simbolos_rx), cfg.bits_por_simbolo))
    d2 = np.abs(simbolos_rx[:, None] - cfg.constelacion[None, :]) ** 2
    for b in range(cfg.bits_por_simbolo):
        idx0 = cfg.etiquetas_bits[:, b] == 0
        idx1 = ~idx0
        llrs[:, b] = np.min(d2[:, idx1], axis=1) / n0 - np.min(d2[:, idx0], axis=1) / n0
    return llrs


def llr_bpsk_exacto(simbolos_rx: np.ndarray, n0: float) -> np.ndarray:
    r = np.real(simbolos_rx)
    return (4.0 * r / n0)[:, None]


def llr_qpsk_exacto(simbolos_rx: np.ndarray, n0: float) -> np.ndarray:
    A = 1.0 / np.sqrt(2.0)
    llr_i = 4.0 * A * np.real(simbolos_rx) / n0
    llr_q = 4.0 * A * np.imag(simbolos_rx) / n0
    return np.column_stack([llr_i, llr_q])


def llr_16qam_exacto(simbolos_rx: np.ndarray, n0: float) -> np.ndarray:
    d = 1.0 / np.sqrt(10.0)
    y_i = np.real(simbolos_rx)
    y_q = np.imag(simbolos_rx)

    def eje_llrs(y: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        l_signo = logsumexp(
            np.column_stack([-(y - d) ** 2 / n0, -(y - 3.0 * d) ** 2 / n0]), axis=1
        ) - logsumexp(
            np.column_stack([-(y + d) ** 2 / n0, -(y + 3.0 * d) ** 2 / n0]), axis=1
        )
        l_amp = logsumexp(
            np.column_stack([-(y - 3.0 * d) ** 2 / n0, -(y + 3.0 * d) ** 2 / n0]), axis=1
        ) - logsumexp(
            np.column_stack([-(y - d) ** 2 / n0, -(y + d) ** 2 / n0]), axis=1
        )
        return l_signo, l_amp

    li0, li1 = eje_llrs(y_i)
    lq0, lq1 = eje_llrs(y_q)
    return np.column_stack([li0, li1, lq0, lq1])


def llr_16qam_maxlog(simbolos_rx: np.ndarray, n0: float) -> np.ndarray:
    d = 1.0 / np.sqrt(10.0)
    y_i = np.real(simbolos_rx)
    y_q = np.imag(simbolos_rx)

    def eje_llrs(y: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        l_signo = (
            np.minimum((y + d) ** 2, (y + 3.0 * d) ** 2)
            - np.minimum((y - d) ** 2, (y - 3.0 * d) ** 2)
        ) / n0
        l_amp = (
            np.minimum((y - d) ** 2, (y + d) ** 2)
            - np.minimum((y - 3.0 * d) ** 2, (y + 3.0 * d) ** 2)
        ) / n0
        return l_signo, l_amp

    li0, li1 = eje_llrs(y_i)
    lq0, lq1 = eje_llrs(y_q)
    return np.column_stack([li0, li1, lq0, lq1])


def calcular_llrs(simbolos_rx: np.ndarray, cfg: ModulationConfig, n0: float) -> Tuple[np.ndarray, np.ndarray]:
    if cfg.nombre == "BPSK":
        exacto = llr_bpsk_exacto(simbolos_rx, n0)
        maxlog = llr_generico_maxlog(simbolos_rx, cfg, n0)
        return exacto, maxlog
    if cfg.nombre == "QPSK":
        exacto = llr_qpsk_exacto(simbolos_rx, n0)
        maxlog = llr_generico_maxlog(simbolos_rx, cfg, n0)
        return exacto, maxlog
    if cfg.nombre == "16-QAM":
        return llr_16qam_exacto(simbolos_rx, n0), llr_16qam_maxlog(simbolos_rx, n0)
    return llr_generico_exacto(simbolos_rx, cfg, n0), llr_generico_maxlog(simbolos_rx, cfg, n0)


# -----------------------------------------------------------------------------
# BER y teoría
# -----------------------------------------------------------------------------


def ber_teorica_awgn(cfg: ModulationConfig, ebn0_db: np.ndarray) -> np.ndarray:
    gamma_b = 10.0 ** (ebn0_db / 10.0)
    if cfg.nombre in {"BPSK", "QPSK"}:
        return qfunc(np.sqrt(2.0 * gamma_b))
    if cfg.nombre == "8-PSK":
        k = cfg.bits_por_simbolo
        return (2.0 / k) * qfunc(np.sqrt(2.0 * k * gamma_b) * np.sin(np.pi / cfg.M))
    if cfg.tipo == "qam":
        k = cfg.bits_por_simbolo
        return (4.0 / k) * (1.0 - 1.0 / np.sqrt(cfg.M)) * qfunc(
            np.sqrt(3.0 * k * gamma_b / (cfg.M - 1.0))
        )
    raise ValueError("Modulación no soportada para teoría AWGN.")


def ber_teorica_bpsk_rayleigh(ebn0_db: np.ndarray) -> np.ndarray:
    gamma_b = 10.0 ** (ebn0_db / 10.0)
    return 0.5 * (1.0 - np.sqrt(gamma_b / (1.0 + gamma_b)))


def simular_ber(
    cfg: ModulationConfig,
    h_rrc: np.ndarray,
    sps: int,
    rs_hz: float,
    fc_hz: float,
    ebn0_db_vec: Iterable[float],
    bits_por_punto: int,
    rng: np.random.Generator,
    canal: str = "awgn",
    cfo_hz: float = 0.0,
    phase_offset_rad: float = 0.0,
    iq_epsilon: float = 0.0,
    iq_phase_rad: float = 0.0,
    K_rician: float = 6.0,
) -> np.ndarray:
    bers = []
    k = cfg.bits_por_simbolo
    nbits_frame = max(2000, int(np.ceil(bits_por_punto / 4 / k)) * k)

    for ebn0_db in ebn0_db_vec:
        errores = 0
        total = 0
        while total < bits_por_punto and errores < max(400, bits_por_punto // 5):
            bits_tx = rng.integers(0, 2, size=nbits_frame, endpoint=False)
            resultado = cadena_tx_ch_rx(
                bits_tx,
                cfg,
                h_rrc,
                sps,
                rs_hz,
                fc_hz,
                canal,
                ebn0_db,
                rng,
                cfo_hz=cfo_hz,
                phase_offset_rad=phase_offset_rad,
                iq_epsilon=iq_epsilon,
                iq_phase_rad=iq_phase_rad,
                K_rician=K_rician,
            )
            bits_rx = hard_demapper(resultado["muestras_eq"], cfg)
            errores += np.count_nonzero(bits_rx != bits_tx)
            total += len(bits_tx)
        bers.append(max(errores, 1) / total if errores == 0 else errores / total)
    return np.asarray(bers)


# -----------------------------------------------------------------------------
# Figuras
# -----------------------------------------------------------------------------


def configurar_axes_constelacion(ax, titulo: str) -> None:
    ax.axhline(0.0, color="0.7", lw=0.8)
    ax.axvline(0.0, color="0.7", lw=0.8)
    ax.set_title(titulo)
    ax.set_xlabel("I")
    ax.set_ylabel("Q")
    ax.grid(True, ls=":")
    ax.set_aspect("equal", adjustable="box")


def plot_constelaciones(modulaciones: Dict[str, ModulationConfig], out_dir: Path) -> None:
    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    axes = axes.ravel()
    nombres = ["BPSK", "QPSK", "8PSK", "16QAM", "64QAM"]
    for ax, nombre in zip(axes, nombres):
        cfg = modulaciones[nombre]
        ax.scatter(np.real(cfg.constelacion), np.imag(cfg.constelacion), s=60, c="tab:blue")
        for s, bits in zip(cfg.constelacion, cfg.etiquetas_bits):
            ax.text(np.real(s) + 0.03, np.imag(s) + 0.03, "".join(map(str, bits.tolist())), fontsize=7)
        configurar_axes_constelacion(ax, cfg.nombre)
    axes[-1].axis("off")
    fig.suptitle("Constelaciones Gray normalizadas")
    fig.tight_layout()
    fig.savefig(out_dir / "constelaciones_gray.png", dpi=180)
    plt.close(fig)


def plot_cadena_pasobanda(
    cfg: ModulationConfig,
    h_rrc: np.ndarray,
    sps: int,
    rs_hz: float,
    fc_hz: float,
    out_dir: Path,
    rng: np.random.Generator,
) -> None:
    bits_tx = rng.integers(0, 2, size=80 * cfg.bits_por_simbolo, endpoint=False)
    resultado = cadena_tx_ch_rx(bits_tx, cfg, h_rrc, sps, rs_hz, fc_hz, "awgn", 18.0, rng)
    tx_bb = resultado["tx_bb"]
    rf = resultado["rf"]
    n_show = min(220, len(rf))
    t = np.arange(n_show) / resultado["fs_hz"]

    fig, axes = plt.subplots(3, 1, figsize=(11, 8), sharex=True)
    axes[0].plot(t, np.real(tx_bb[:n_show]), label="I(t)")
    axes[0].plot(t, np.imag(tx_bb[:n_show]), label="Q(t)")
    axes[0].set_title("Señal pasabaja compleja tras RRC")
    axes[0].set_ylabel("Amplitud")
    axes[0].grid(True, ls=":")
    axes[0].legend()

    axes[1].plot(t, rf[:n_show], color="tab:red")
    axes[1].set_title("Señal pasabanda real transmitida")
    axes[1].set_ylabel("s_RF(t)")
    axes[1].grid(True, ls=":")

    muestras = resultado["muestras_eq"][:80]
    axes[2].scatter(np.real(muestras), np.imag(muestras), s=15, alpha=0.8)
    configurar_axes_constelacion(axes[2], "Muestras Rx tras filtro adaptado")
    axes[2].set_xlabel("I")
    fig.tight_layout()
    fig.savefig(out_dir / "cadena_pasobanda_qpsk.png", dpi=180)
    plt.close(fig)


def plot_constelacion_impairment(
    cfg: ModulationConfig,
    h_rrc: np.ndarray,
    sps: int,
    rs_hz: float,
    fc_hz: float,
    out_path: Path,
    rng: np.random.Generator,
    titulo: str,
    cfo_hz: float = 0.0,
    phase_offset_rad: float = 0.0,
    iq_epsilon: float = 0.0,
    iq_phase_rad: float = 0.0,
) -> None:
    bits_tx = rng.integers(0, 2, size=600 * cfg.bits_por_simbolo, endpoint=False)
    resultado = cadena_tx_ch_rx(
        bits_tx,
        cfg,
        h_rrc,
        sps,
        rs_hz,
        fc_hz,
        "awgn",
        22.0,
        rng,
        cfo_hz=cfo_hz,
        phase_offset_rad=phase_offset_rad,
        iq_epsilon=iq_epsilon,
        iq_phase_rad=iq_phase_rad,
    )
    muestras = resultado["muestras_eq"]
    colores = np.linspace(0.0, 1.0, len(muestras))

    fig, ax = plt.subplots(figsize=(7, 6))
    sc = ax.scatter(np.real(muestras), np.imag(muestras), c=colores, cmap="viridis", s=10, alpha=0.75)
    fig.colorbar(sc, ax=ax, label="Índice temporal")
    configurar_axes_constelacion(ax, titulo)
    fig.tight_layout()
    fig.savefig(out_path, dpi=180)
    plt.close(fig)


def plot_llr_distribuciones(
    cfg: ModulationConfig,
    h_rrc: np.ndarray,
    sps: int,
    rs_hz: float,
    fc_hz: float,
    out_dir: Path,
    rng: np.random.Generator,
    snrs_db: Tuple[float, float] = (4.0, 12.0),
) -> None:
    fig, axes = plt.subplots(len(snrs_db), 2, figsize=(11, 7), sharex="col")
    bits_tx = rng.integers(0, 2, size=4000 * cfg.bits_por_simbolo, endpoint=False)
    for fila, snr_db in enumerate(snrs_db):
        resultado = cadena_tx_ch_rx(bits_tx, cfg, h_rrc, sps, rs_hz, fc_hz, "awgn", snr_db, rng)
        exacto, maxlog = calcular_llrs(resultado["muestras_eq"], cfg, resultado["n0"])
        bits_matriz = bits_tx.reshape(-1, cfg.bits_por_simbolo)
        bit0 = bits_matriz[:, 0]

        axes[fila, 0].hist(exacto[bit0 == 0, 0], bins=50, alpha=0.6, label="b=0", density=True)
        axes[fila, 0].hist(exacto[bit0 == 1, 0], bins=50, alpha=0.6, label="b=1", density=True)
        axes[fila, 0].set_title(f"{cfg.nombre} - LLR exacto @ {snr_db:.0f} dB")
        axes[fila, 0].grid(True, ls=":")
        axes[fila, 0].legend()

        axes[fila, 1].hist(maxlog[bit0 == 0, 0], bins=50, alpha=0.6, label="b=0", density=True)
        axes[fila, 1].hist(maxlog[bit0 == 1, 0], bins=50, alpha=0.6, label="b=1", density=True)
        axes[fila, 1].set_title(f"{cfg.nombre} - LLR max-log @ {snr_db:.0f} dB")
        axes[fila, 1].grid(True, ls=":")
        axes[fila, 1].legend()

    for ax in axes[-1, :]:
        ax.set_xlabel("LLR")
    for ax in axes[:, 0]:
        ax.set_ylabel("Densidad")

    fig.tight_layout()
    nombre = cfg.nombre.lower().replace("-", "").replace(" ", "_")
    fig.savefig(out_dir / f"llr_{nombre}.png", dpi=180)
    plt.close(fig)


def plot_ber_awgn(
    modulaciones: Dict[str, ModulationConfig],
    h_rrc: np.ndarray,
    sps: int,
    rs_hz: float,
    fc_hz: float,
    out_dir: Path,
    rng: np.random.Generator,
    ebn0_db: np.ndarray,
    bits_por_punto: int,
) -> None:
    fig, ax = plt.subplots(figsize=(9, 6))
    for nombre, cfg in modulaciones.items():
        ber_sim = simular_ber(cfg, h_rrc, sps, rs_hz, fc_hz, ebn0_db, bits_por_punto, rng, canal="awgn")
        ber_th = ber_teorica_awgn(cfg, ebn0_db)
        ax.semilogy(ebn0_db, ber_sim, "o-", label=f"{cfg.nombre} sim")
        ax.semilogy(ebn0_db, ber_th, "--", label=f"{cfg.nombre} teoría")
    ax.set_xlabel(r"$E_b/N_0$ [dB]")
    ax.set_ylabel("BER")
    ax.set_title("BER vs $E_b/N_0$ en AWGN")
    ax.grid(True, which="both", ls=":")
    ax.legend(ncol=2, fontsize=8)
    fig.tight_layout()
    fig.savefig(out_dir / "ber_awgn_todas_modulaciones.png", dpi=180)
    plt.close(fig)


def plot_ber_canales(
    cfg: ModulationConfig,
    h_rrc: np.ndarray,
    sps: int,
    rs_hz: float,
    fc_hz: float,
    out_dir: Path,
    rng: np.random.Generator,
    ebn0_db: np.ndarray,
    bits_por_punto: int,
) -> None:
    fig, ax = plt.subplots(figsize=(8.5, 6))
    for canal in ["awgn", "rayleigh", "rician"]:
        ber = simular_ber(cfg, h_rrc, sps, rs_hz, fc_hz, ebn0_db, bits_por_punto, rng, canal=canal)
        ax.semilogy(ebn0_db, ber, "o-", label=f"{canal.capitalize()} sim")
    ax.semilogy(ebn0_db, ber_teorica_awgn(cfg, ebn0_db), "k--", lw=1.2, label="AWGN teoría")
    ax.semilogy(ebn0_db, ber_teorica_bpsk_rayleigh(ebn0_db), "k:", lw=1.5, label="Rayleigh teoría")
    ax.set_xlabel(r"$E_b/N_0$ [dB]")
    ax.set_ylabel("BER")
    ax.set_title("Comparación de canal para BPSK coherente")
    ax.grid(True, which="both", ls=":")
    ax.legend()
    fig.tight_layout()
    fig.savefig(out_dir / "ber_bpsk_canales.png", dpi=180)
    plt.close(fig)


def plot_ber_impairments(
    modulaciones: Dict[str, ModulationConfig],
    h_rrc: np.ndarray,
    sps: int,
    rs_hz: float,
    fc_hz: float,
    out_dir: Path,
    rng: np.random.Generator,
    bits_por_punto: int,
    ebn0_ref_db: float,
) -> None:
    fig, axes = plt.subplots(2, 2, figsize=(12, 9))

    cfo_norm = np.array([0.0, 0.002, 0.005, 0.01, 0.02, 0.03])
    phase_deg = np.array([0, 3, 6, 10, 15, 20, 30])
    iq_eps = np.array([0.0, 0.02, 0.05, 0.08, 0.12, 0.16, 0.2])
    iq_phi_deg = np.array([0.0, 1.0, 2.0, 4.0, 6.0, 8.0, 10.0])

    for nombre, cfg in modulaciones.items():
        ber_cfo = [
            simular_ber(cfg, h_rrc, sps, rs_hz, fc_hz, [ebn0_ref_db], bits_por_punto, rng, cfo_hz=val * rs_hz)[0]
            for val in cfo_norm
        ]
        axes[0, 0].semilogy(cfo_norm, ber_cfo, "o-", label=cfg.nombre)

        ber_phase = [
            simular_ber(cfg, h_rrc, sps, rs_hz, fc_hz, [ebn0_ref_db], bits_por_punto, rng, phase_offset_rad=np.deg2rad(val))[0]
            for val in phase_deg
        ]
        axes[0, 1].semilogy(phase_deg, ber_phase, "o-", label=cfg.nombre)

        ber_iq_gain = [
            simular_ber(
                cfg,
                h_rrc,
                sps,
                rs_hz,
                fc_hz,
                [ebn0_ref_db],
                bits_por_punto,
                rng,
                iq_epsilon=val,
                iq_phase_rad=np.deg2rad(5.0),
            )[0]
            for val in iq_eps
        ]
        axes[1, 0].semilogy(iq_eps, ber_iq_gain, "o-", label=cfg.nombre)

        ber_iq_phase = [
            simular_ber(
                cfg,
                h_rrc,
                sps,
                rs_hz,
                fc_hz,
                [ebn0_ref_db],
                bits_por_punto,
                rng,
                iq_epsilon=0.08,
                iq_phase_rad=np.deg2rad(val),
            )[0]
            for val in iq_phi_deg
        ]
        axes[1, 1].semilogy(iq_phi_deg, ber_iq_phase, "o-", label=cfg.nombre)

    titulos = [
        r"BER vs CFO normalizado $\Delta f T_s$",
        "BER vs offset de fase",
        "BER vs ganancia IQ ε (φ_IQ=5°)",
        "BER vs fase IQ φ_IQ (ε=0.08)",
    ]
    xlabels = [r"$\Delta f T_s$", "Fase [°]", r"$\epsilon$", r"$\phi_{IQ}$ [°]"]

    for ax, titulo, xlabel in zip(axes.ravel(), titulos, xlabels):
        ax.set_title(titulo)
        ax.set_xlabel(xlabel)
        ax.set_ylabel("BER")
        ax.grid(True, which="both", ls=":")
        ax.legend(fontsize=8)

    fig.tight_layout()
    fig.savefig(out_dir / "ber_impairments_por_modulacion.png", dpi=180)
    plt.close(fig)


def plot_ber_combined_impairments(
    cfg: ModulationConfig,
    h_rrc: np.ndarray,
    sps: int,
    rs_hz: float,
    fc_hz: float,
    out_dir: Path,
    rng: np.random.Generator,
    bits_por_punto: int,
    ebn0_ref_db: float,
) -> None:
    severidad = np.array([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ber = []
    for s in severidad:
        ber.append(
            simular_ber(
                cfg,
                h_rrc,
                sps,
                rs_hz,
                fc_hz,
                [ebn0_ref_db],
                bits_por_punto,
                rng,
                cfo_hz=0.02 * s * rs_hz,
                phase_offset_rad=np.deg2rad(18.0 * s),
                iq_epsilon=0.12 * s,
                iq_phase_rad=np.deg2rad(7.0 * s),
            )[0]
        )

    fig, ax = plt.subplots(figsize=(8, 5.5))
    ax.semilogy(severidad, ber, "o-", color="tab:red")
    ax.set_title(f"Degradación BER con impairments combinados ({cfg.nombre})")
    ax.set_xlabel("Severidad combinada normalizada")
    ax.set_ylabel("BER")
    ax.grid(True, which="both", ls=":")
    fig.tight_layout()
    fig.savefig(out_dir / "ber_impairments_combinados_16qam.png", dpi=180)
    plt.close(fig)


# -----------------------------------------------------------------------------
# Parámetros y programa principal
# -----------------------------------------------------------------------------


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Simulación de modulación digital con impairments para la Unidad 3."
    )
    parser.add_argument("--output-dir", default=None, help="Directorio de salida para figuras.")
    parser.add_argument("--seed", type=int, default=1234, help="Semilla del generador aleatorio.")
    parser.add_argument("--rolloff", type=float, default=0.25, help="Factor de roll-off del RRC.")
    parser.add_argument("--span", type=int, default=8, help="Span del RRC en símbolos.")
    parser.add_argument("--sps", type=int, default=8, help="Muestras por símbolo.")
    parser.add_argument("--rs-hz", type=float, default=1000.0, help="Tasa de símbolo en Hz.")
    parser.add_argument("--fc-hz", type=float, default=2200.0, help="Frecuencia portadora en Hz.")
    parser.add_argument("--bits-ber", type=int, default=24000, help="Bits por punto BER en modo completo.")
    parser.add_argument(
        "--modo-rapido",
        action="store_true",
        help="Reduce el número de bits y puntos para validación rápida.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    base_dir = Path(__file__).resolve().parent
    out_dir = Path(args.output_dir) if args.output_dir else base_dir / "figuras"
    out_dir.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(args.seed)
    modulaciones = obtener_modulaciones()
    h_rrc = rrc_filter(args.rolloff, args.span, args.sps)

    if args.fc_hz >= args.rs_hz * args.sps / 2.0:
        raise ValueError("La portadora debe ser menor que fs/2.")

    if args.modo_rapido:
        ebn0_db = np.array([0.0, 4.0, 8.0, 12.0])
        bits_por_punto = min(args.bits_ber, 8000)
    else:
        ebn0_db = np.arange(0.0, 17.0, 2.0)
        bits_por_punto = args.bits_ber

    plot_constelaciones(modulaciones, out_dir)
    plot_cadena_pasobanda(modulaciones["QPSK"], h_rrc, args.sps, args.rs_hz, args.fc_hz, out_dir, rng)

    plot_constelacion_impairment(
        modulaciones["QPSK"],
        h_rrc,
        args.sps,
        args.rs_hz,
        args.fc_hz,
        out_dir / "constelacion_cfo.png",
        rng,
        titulo="QPSK con CFO: giro de constelación",
        cfo_hz=0.03 * args.rs_hz,
    )
    plot_constelacion_impairment(
        modulaciones["16QAM"],
        h_rrc,
        args.sps,
        args.rs_hz,
        args.fc_hz,
        out_dir / "constelacion_phase_offset.png",
        rng,
        titulo="16-QAM con offset de fase",
        phase_offset_rad=np.deg2rad(25.0),
    )
    plot_constelacion_impairment(
        modulaciones["16QAM"],
        h_rrc,
        args.sps,
        args.rs_hz,
        args.fc_hz,
        out_dir / "constelacion_iq_imbalance.png",
        rng,
        titulo="16-QAM con desbalance I/Q",
        iq_epsilon=0.12,
        iq_phase_rad=np.deg2rad(7.0),
    )
    plot_constelacion_impairment(
        modulaciones["16QAM"],
        h_rrc,
        args.sps,
        args.rs_hz,
        args.fc_hz,
        out_dir / "constelacion_impairments_combinados.png",
        rng,
        titulo="16-QAM con impairments combinados",
        cfo_hz=0.02 * args.rs_hz,
        phase_offset_rad=np.deg2rad(15.0),
        iq_epsilon=0.1,
        iq_phase_rad=np.deg2rad(6.0),
    )

    for nombre in ["BPSK", "QPSK", "16QAM"]:
        plot_llr_distribuciones(
            modulaciones[nombre], h_rrc, args.sps, args.rs_hz, args.fc_hz, out_dir, rng
        )

    plot_ber_awgn(
        modulaciones,
        h_rrc,
        args.sps,
        args.rs_hz,
        args.fc_hz,
        out_dir,
        rng,
        ebn0_db,
        bits_por_punto,
    )
    plot_ber_canales(
        modulaciones["BPSK"],
        h_rrc,
        args.sps,
        args.rs_hz,
        args.fc_hz,
        out_dir,
        rng,
        ebn0_db,
        bits_por_punto,
    )
    plot_ber_impairments(
        modulaciones,
        h_rrc,
        args.sps,
        args.rs_hz,
        args.fc_hz,
        out_dir,
        rng,
        bits_por_punto=max(4000, bits_por_punto // 2),
        ebn0_ref_db=12.0,
    )
    plot_ber_combined_impairments(
        modulaciones["16QAM"],
        h_rrc,
        args.sps,
        args.rs_hz,
        args.fc_hz,
        out_dir,
        rng,
        bits_por_punto=max(4000, bits_por_punto // 2),
        ebn0_ref_db=12.0,
    )

    print(f"Simulación completada. Figuras guardadas en: {out_dir}")


if __name__ == "__main__":
    main()
