#!/usr/bin/env python3
"""Simulaciones de la Unidad 2: Teoría de Información y Codificación de Fuente."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
import numpy as np
from scipy import special


SCRIPT_DIR = Path(__file__).resolve().parent
FIG_DIR = SCRIPT_DIR / "figuras"
EPS = 1e-12


# =========================
# Utilidades generales
# =========================
def configurar_estilo() -> None:
    """Configura un estilo consistente para todas las figuras."""
    plt.rcParams.update(
        {
            "figure.dpi": 130,
            "savefig.dpi": 220,
            "axes.grid": True,
            "grid.alpha": 0.25,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "font.size": 10,
        }
    )


def asegurar_directorios() -> None:
    """Crea el directorio de salida si no existe."""
    FIG_DIR.mkdir(parents=True, exist_ok=True)


def guardar_figura(fig: plt.Figure, nombre: str) -> Path:
    """Guarda una figura en el directorio figuras/."""
    ruta = FIG_DIR / nombre
    fig.tight_layout()
    fig.savefig(ruta, bbox_inches="tight")
    plt.close(fig)
    return ruta


def log2_seguro(x: np.ndarray | float) -> np.ndarray | float:
    """Evita logaritmos de cero usando un piso numérico."""
    return np.log2(np.maximum(x, EPS))


def db10(x: np.ndarray | float) -> np.ndarray | float:
    """Convierte una razón lineal a dB."""
    return 10.0 * np.log10(np.maximum(x, EPS))


def qfunc(x: np.ndarray | float) -> np.ndarray | float:
    """Función Q gaussiana."""
    return 0.5 * special.erfc(np.asarray(x) / np.sqrt(2.0))


# =========================
# Medidas de información
# =========================
def self_information(probabilidades: np.ndarray) -> np.ndarray:
    """Calcula autoinformación en bits."""
    probabilidades = np.asarray(probabilidades, dtype=float)
    return -log2_seguro(probabilidades)


def entropy(probabilidades: np.ndarray) -> float:
    """Calcula entropía de Shannon en bits."""
    p = np.asarray(probabilidades, dtype=float)
    p = p[p > 0]
    return float(-np.sum(p * np.log2(p)))


def joint_entropy(prob_conjunta: np.ndarray) -> float:
    """Calcula entropía conjunta H(X,Y)."""
    pxy = np.asarray(prob_conjunta, dtype=float)
    pxy = pxy[pxy > 0]
    return float(-np.sum(pxy * np.log2(pxy)))


def conditional_entropy(prob_conjunta: np.ndarray, axis: int = 0) -> float:
    """Calcula H(Y|X) si axis=0, o H(X|Y) si axis=1."""
    pxy = np.asarray(prob_conjunta, dtype=float)
    if axis == 0:
        marginal = pxy.sum(axis=1, keepdims=True)
    else:
        marginal = pxy.sum(axis=0, keepdims=True)
    cond = np.divide(pxy, marginal, out=np.zeros_like(pxy), where=marginal > 0)
    mascara = pxy > 0
    return float(-np.sum(pxy[mascara] * np.log2(np.maximum(cond[mascara], EPS))))


def mutual_information(prob_conjunta: np.ndarray) -> float:
    """Calcula información mutua I(X;Y)."""
    pxy = np.asarray(prob_conjunta, dtype=float)
    px = pxy.sum(axis=1, keepdims=True)
    py = pxy.sum(axis=0, keepdims=True)
    producto = px @ py
    mascara = pxy > 0
    return float(np.sum(pxy[mascara] * np.log2(np.maximum(pxy[mascara] / producto[mascara], EPS))))


def binary_entropy(p: np.ndarray | float) -> np.ndarray | float:
    """Entropía binaria H2(p)."""
    p = np.asarray(p, dtype=float)
    return -(p * log2_seguro(p) + (1.0 - p) * log2_seguro(1.0 - p))


def demo_medidas_informacion(rng: np.random.Generator) -> list[Path]:
    """Genera figuras de autoinformación, entropía, medidas conjuntas y diagrama de Venn."""
    rutas = []

    distribuciones = {
        "Determinista": np.array([1.0, 0.0, 0.0, 0.0]),
        "Sesgada": np.array([0.7, 0.15, 0.10, 0.05]),
        "Casi uniforme": np.array([0.30, 0.25, 0.24, 0.21]),
        "Uniforme": np.full(4, 0.25),
    }

    fig, ax = plt.subplots(figsize=(8, 4.5))
    probs_demo = np.linspace(0.01, 1.0, 400)
    ax.plot(probs_demo, self_information(probs_demo), lw=2.2, color="tab:blue")
    puntos = np.array([0.5, 0.25, 0.125, 0.05])
    ax.scatter(puntos, self_information(puntos), color="tab:red", zorder=3)
    for p in puntos:
        ax.annotate(f"p={p:.3f}", (p, float(self_information(p))), textcoords="offset points", xytext=(6, 5))
    ax.set_title("Autoinformación I(x) = -log2 p(x)")
    ax.set_xlabel("Probabilidad del suceso")
    ax.set_ylabel("Bits")
    rutas.append(guardar_figura(fig, "unidad2_info_autoinformacion.png"))

    nombres = list(distribuciones.keys())
    entropias = [entropy(p) for p in distribuciones.values()]
    fig, ax = plt.subplots(figsize=(8, 4.5))
    barras = ax.bar(nombres, entropias, color=["tab:gray", "tab:orange", "tab:green", "tab:blue"])
    ax.axhline(np.log2(4), color="k", ls="--", lw=1.4, label="log2(4) = 2 bits")
    ax.set_ylabel("Entropía [bits]")
    ax.set_title("Entropía para distintas distribuciones")
    ax.legend()
    for barra, valor in zip(barras, entropias):
        ax.text(barra.get_x() + barra.get_width() / 2, valor + 0.03, f"{valor:.2f}", ha="center")
    rutas.append(guardar_figura(fig, "unidad2_info_entropias_distribuciones.png"))

    muestras = rng.dirichlet(alpha=np.ones(4), size=2500)
    ent_muestras = np.apply_along_axis(entropy, 1, muestras)
    dist_uniforme = np.linalg.norm(muestras - 0.25, axis=1)
    fig, ax = plt.subplots(figsize=(7.5, 4.8))
    ax.scatter(dist_uniforme, ent_muestras, s=12, alpha=0.35, color="tab:purple", label="Distribuciones aleatorias")
    ax.scatter([0.0], [entropy(np.full(4, 0.25))], s=85, color="crimson", label="Distribución uniforme")
    ax.set_xlabel("Distancia euclídea a la distribución uniforme")
    ax.set_ylabel("Entropía [bits]")
    ax.set_title("Prueba numérica: la distribución uniforme maximiza H(X)")
    ax.legend()
    rutas.append(guardar_figura(fig, "unidad2_info_maximo_entropia_uniforme.png"))

    pxy = np.array([[0.4, 0.1], [0.2, 0.3]])
    px = pxy.sum(axis=1)
    py = pxy.sum(axis=0)
    hx = entropy(px)
    hy = entropy(py)
    hxy = joint_entropy(pxy)
    hyx = conditional_entropy(pxy, axis=0)
    hxy_cond = conditional_entropy(pxy, axis=1)
    ixy = mutual_information(pxy)

    medidas = {
        "H(X)": hx,
        "H(Y)": hy,
        "H(X,Y)": hxy,
        "H(Y|X)": hyx,
        "H(X|Y)": hxy_cond,
        "I(X;Y)": ixy,
    }
    fig, ax = plt.subplots(figsize=(8, 4.8))
    barras = ax.bar(list(medidas.keys()), list(medidas.values()), color="tab:cyan")
    ax.set_ylabel("Bits")
    ax.set_title("Entropía conjunta, condicional e información mutua")
    for barra, valor in zip(barras, medidas.values()):
        ax.text(barra.get_x() + barra.get_width() / 2, valor + 0.02, f"{valor:.3f}", ha="center", fontsize=9)
    rutas.append(guardar_figura(fig, "unidad2_info_medidas_conjuntas.png"))

    fig, ax = plt.subplots(figsize=(6.5, 4.8))
    ax.set_aspect("equal")
    ax.add_patch(Circle((0.42, 0.5), 0.28, color="tab:blue", alpha=0.28))
    ax.add_patch(Circle((0.62, 0.5), 0.28, color="tab:orange", alpha=0.28))
    ax.text(0.28, 0.5, f"H(X|Y)\n{hxy_cond:.3f}", ha="center", va="center", fontsize=11)
    ax.text(0.72, 0.5, f"H(Y|X)\n{hyx:.3f}", ha="center", va="center", fontsize=11)
    ax.text(0.52, 0.5, f"I(X;Y)\n{ixy:.3f}", ha="center", va="center", fontsize=11, weight="bold")
    ax.text(0.42, 0.83, f"H(X)={hx:.3f}", ha="center", fontsize=11)
    ax.text(0.62, 0.83, f"H(Y)={hy:.3f}", ha="center", fontsize=11)
    ax.text(0.52, 0.16, f"H(X,Y)={hxy:.3f}", ha="center", fontsize=11)
    ax.set_xlim(0.05, 0.95)
    ax.set_ylim(0.1, 0.95)
    ax.axis("off")
    ax.set_title("Diagrama tipo Venn de medidas de información")
    rutas.append(guardar_figura(fig, "unidad2_info_diagrama_venn.png"))

    return rutas


# =========================
# PCM y codificación de fuente
# =========================
def generar_senal_analogica(fs_cont: float = 20000.0, duracion: float = 0.02) -> tuple[np.ndarray, np.ndarray]:
    """Genera una señal de prueba limitada en banda."""
    t = np.arange(0.0, duracion, 1.0 / fs_cont)
    x = 0.72 * np.sin(2 * np.pi * 300 * t) + 0.28 * np.sin(2 * np.pi * 600 * t + 0.35)
    return t, x


def muestrear_senal(t: np.ndarray, x: np.ndarray, fs: float) -> tuple[np.ndarray, np.ndarray]:
    """Obtiene muestras uniformes a partir de una señal continua densa."""
    duracion = t[-1] + (t[1] - t[0])
    ts = np.arange(0.0, duracion, 1.0 / fs)
    xs = np.interp(ts, t, x)
    return ts, xs


def reconstruccion_sinc(ts: np.ndarray, xs: np.ndarray, t_eval: np.ndarray, fs: float) -> np.ndarray:
    """Reconstrucción ideal aproximada mediante interpolación sinc."""
    matriz = np.sinc(fs * (t_eval[:, None] - ts[None, :]))
    return matriz @ xs


def cuantizador_uniforme(x: np.ndarray, bits: int, xmin: float = -1.0, xmax: float = 1.0) -> tuple[np.ndarray, np.ndarray, float]:
    """Cuantizador uniforme tipo mid-rise."""
    niveles = 2 ** bits
    delta = (xmax - xmin) / niveles
    x_clip = np.clip(x, xmin, xmax - EPS)
    indices = np.floor((x_clip - xmin) / delta).astype(int)
    xq = xmin + (indices + 0.5) * delta
    return xq, indices, delta


def ley_mu(x: np.ndarray, mu: float = 255.0) -> np.ndarray:
    """Compresión mu-law."""
    x = np.clip(np.asarray(x, dtype=float), -1.0, 1.0)
    return np.sign(x) * np.log1p(mu * np.abs(x)) / np.log1p(mu)


def inv_ley_mu(y: np.ndarray, mu: float = 255.0) -> np.ndarray:
    """Expansión inversa mu-law."""
    y = np.clip(np.asarray(y, dtype=float), -1.0, 1.0)
    return np.sign(y) * (np.expm1(np.abs(y) * np.log1p(mu)) / mu)


def ley_a(x: np.ndarray, a: float = 87.6) -> np.ndarray:
    """Compresión A-law."""
    x = np.clip(np.asarray(x, dtype=float), -1.0, 1.0)
    ax = np.abs(x)
    denom = 1.0 + np.log(a)
    y = np.empty_like(x)
    mascara = ax < (1.0 / a)
    y[mascara] = np.sign(x[mascara]) * (a * ax[mascara]) / denom
    y[~mascara] = np.sign(x[~mascara]) * (1.0 + np.log(a * ax[~mascara])) / denom
    return y


def inv_ley_a(y: np.ndarray, a: float = 87.6) -> np.ndarray:
    """Expansión inversa A-law."""
    y = np.clip(np.asarray(y, dtype=float), -1.0, 1.0)
    ay = np.abs(y)
    umbral = 1.0 / (1.0 + np.log(a))
    x = np.empty_like(y)
    mascara = ay < umbral
    x[mascara] = np.sign(y[mascara]) * ay[mascara] * (1.0 + np.log(a)) / a
    x[~mascara] = np.sign(y[~mascara]) * np.exp(ay[~mascara] * (1.0 + np.log(a)) - 1.0) / a
    return x


def sqnr_db(x: np.ndarray, xq: np.ndarray) -> float:
    """Calcula SQNR en dB."""
    potencia_senal = np.mean(np.asarray(x) ** 2)
    potencia_ruido = np.mean((np.asarray(x) - np.asarray(xq)) ** 2)
    return float(db10(potencia_senal / np.maximum(potencia_ruido, EPS)))


def demo_pcm() -> list[Path]:
    """Genera figuras del teorema de muestreo, cuantización y cadena PCM."""
    rutas = []
    t, x = generar_senal_analogica()

    fs_list = [900.0, 1200.0, 2400.0]
    fig, axes = plt.subplots(len(fs_list), 1, figsize=(9, 7), sharex=True)
    for ax, fs in zip(axes, fs_list):
        ts, xs = muestrear_senal(t, x, fs)
        xr = reconstruccion_sinc(ts, xs, t, fs)
        mse = np.mean((x - xr) ** 2)
        ax.plot(t * 1e3, x, label="Señal original", color="tab:blue", lw=2)
        ax.plot(t * 1e3, xr, label="Reconstrucción sinc", color="tab:green", ls="--")
        ax.stem(ts * 1e3, xs, basefmt=" ", linefmt="tab:red", markerfmt="ro")
        ax.set_title(f"Muestreo a fs={fs:.0f} Hz | error cuadrático medio={mse:.4e}")
        ax.set_ylabel("Amplitud")
        ax.legend(loc="upper right", fontsize=8)
    axes[-1].set_xlabel("Tiempo [ms]")
    fig.suptitle("Demostración de Nyquist-Shannon", y=1.02, fontsize=12)
    rutas.append(guardar_figura(fig, "unidad2_pcm_nyquist_demo.png"))

    x_local = np.linspace(-1.0, 1.0, 2000)
    y_mu = ley_mu(x_local)
    y_a = ley_a(x_local)
    fig, ax = plt.subplots(figsize=(7.6, 5))
    ax.plot(x_local, x_local, label="Lineal", color="black", lw=1.5)
    ax.plot(x_local, y_mu, label="Ley-μ (μ=255)", lw=2)
    ax.plot(x_local, y_a, label="Ley-A (A=87.6)", lw=2)
    ax.set_title("Compansión no uniforme: Ley-μ y Ley-A")
    ax.set_xlabel("Entrada normalizada")
    ax.set_ylabel("Salida comprimida")
    ax.legend()
    rutas.append(guardar_figura(fig, "unidad2_pcm_compansion.png"))

    bits = np.arange(2, 9)
    seno = 0.95 * np.sin(2 * np.pi * 13 * np.linspace(0.0, 1.0, 4096, endpoint=False))
    sqnr_sim = []
    for nbits in bits:
        xq, _, _ = cuantizador_uniforme(seno, nbits)
        sqnr_sim.append(sqnr_db(seno, xq))
    sqnr_sim = np.array(sqnr_sim)
    sqnr_teo = 6.02 * bits + 1.76
    fig, ax = plt.subplots(figsize=(7.4, 4.7))
    ax.plot(bits, sqnr_teo, "o-", label="Teoría 6.02n + 1.76")
    ax.plot(bits, sqnr_sim, "s--", label="Simulación senoide")
    ax.set_title("SQNR vs número de bits de cuantización")
    ax.set_xlabel("Bits por muestra")
    ax.set_ylabel("SQNR [dB]")
    ax.legend()
    rutas.append(guardar_figura(fig, "unidad2_pcm_sqnr_vs_bits.png"))

    ts, xs = muestrear_senal(t, x, 1600.0)
    x_muestras = xs[:24]
    xq_uni, idx_uni, delta = cuantizador_uniforme(x_muestras, bits=3)
    x_comp_mu = ley_mu(x_muestras)
    xq_mu_comp, idx_mu, _ = cuantizador_uniforme(x_comp_mu, bits=3)
    xq_mu = inv_ley_mu(xq_mu_comp)
    x_comp_a = ley_a(x_muestras)
    xq_a_comp, idx_a, _ = cuantizador_uniforme(x_comp_a, bits=3)
    xq_a = inv_ley_a(xq_a_comp)

    fig, axes = plt.subplots(2, 1, figsize=(9, 7), sharex=True)
    axes[0].plot(x_muestras, label="Muestras originales", lw=2, marker="o")
    axes[0].step(np.arange(len(xq_uni)), xq_uni, where="mid", label="Cuantización uniforme", lw=2)
    axes[0].step(np.arange(len(xq_mu)), xq_mu, where="mid", label="Cuantización con μ-law", lw=1.8)
    axes[0].step(np.arange(len(xq_a)), xq_a, where="mid", label="Cuantización con A-law", lw=1.8)
    axes[0].set_title("Comparación uniforme vs no uniforme sobre las primeras muestras")
    axes[0].set_ylabel("Amplitud")
    axes[0].legend(ncol=2, fontsize=8)

    codigos = [format(indice, "03b") for indice in idx_uni[:8]]
    axes[1].axis("off")
    tabla = [
        [str(i), f"{x_muestras[i]:+.3f}", f"{xq_uni[i]:+.3f}", str(idx_uni[i]), codigos[i]]
        for i in range(8)
    ]
    axes[1].table(
        cellText=tabla,
        colLabels=["n", "x[n]", "xq[n]", "Nivel", "Código PCM"],
        loc="center",
        cellLoc="center",
    )
    axes[1].set_title(
        f"Cadena PCM (3 bits, Δ={delta:.3f}) | SQNR uniforme={sqnr_db(x_muestras, xq_uni):.2f} dB",
        pad=12,
    )
    rutas.append(guardar_figura(fig, "unidad2_pcm_cadena_pcm.png"))

    return rutas


# =========================
# Capacidad de canal
# =========================
def capacidad_bsc(p: np.ndarray) -> np.ndarray:
    """Capacidad del canal simétrico binario."""
    return 1.0 - binary_entropy(p)


def capacidad_bec(epsilon: np.ndarray) -> np.ndarray:
    """Capacidad del canal con borrados binario."""
    return 1.0 - epsilon


def capacidad_awgn(banda_hz: float, snr_lineal: np.ndarray) -> np.ndarray:
    """Capacidad Shannon-Hartley para AWGN."""
    return banda_hz * np.log2(1.0 + snr_lineal)


def demo_capacidad_canal() -> list[Path]:
    """Genera figuras de BSC, BEC, AWGN y límite de Shannon."""
    rutas = []

    p = np.linspace(1e-4, 0.5, 500)
    eps = np.linspace(0.0, 1.0, 500)
    fig, ax = plt.subplots(figsize=(7.6, 4.8))
    ax.plot(p, capacidad_bsc(p), label="BSC: C = 1 - H2(p)", lw=2)
    ax.plot(eps, capacidad_bec(eps), label="BEC: C = 1 - ε", lw=2)
    ax.set_xlabel("Probabilidad de cruce / borrado")
    ax.set_ylabel("Capacidad [bit/uso]")
    ax.set_title("Capacidad de canales discretos elementales")
    ax.legend()
    rutas.append(guardar_figura(fig, "unidad2_capacidad_bsc_bec.png"))

    snr_db = np.linspace(-10.0, 30.0, 500)
    snr_lin = 10 ** (snr_db / 10.0)
    banda = 1e6
    c_awgn = capacidad_awgn(banda, snr_lin) / 1e6
    eficiencia = np.log2(1.0 + snr_lin)
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.3))
    axes[0].plot(snr_db, c_awgn, color="tab:green", lw=2)
    axes[0].set_title("Capacidad AWGN para B = 1 MHz")
    axes[0].set_xlabel("SNR [dB]")
    axes[0].set_ylabel("Capacidad [Mbit/s]")
    axes[1].plot(snr_db, eficiencia, color="tab:orange", lw=2)
    axes[1].set_title("Eficiencia espectral equivalente")
    axes[1].set_xlabel("SNR [dB]")
    axes[1].set_ylabel("bit/s/Hz")
    rutas.append(guardar_figura(fig, "unidad2_capacidad_awgn.png"))

    eta = np.linspace(0.05, 8.0, 500)
    ebn0_min = (2 ** eta - 1.0) / eta
    fig, ax = plt.subplots(figsize=(7.8, 5.0))
    ax.plot(db10(ebn0_min), eta, lw=2, label="Frontera de Shannon")
    ax.axvline(db10(np.log(2.0)), color="crimson", ls="--", lw=1.8, label="Eb/N0 mínimo = -1.59 dB")
    ax.fill_betweenx(eta, db10(ebn0_min), 14, alpha=0.15, color="tab:green", label="Región factible")
    ax.set_xlim(-2.5, 14.0)
    ax.set_xlabel("Eb/N0 [dB]")
    ax.set_ylabel("Eficiencia espectral [bit/s/Hz]")
    ax.set_title("Plano de Shannon y límite fundamental de potencia")
    ax.legend(loc="upper left", fontsize=8)
    rutas.append(guardar_figura(fig, "unidad2_capacidad_limite_shannon.png"))

    return rutas


# =========================
# Detección digital óptima
# =========================
def pdf_normal(x: np.ndarray, media: float, sigma: float) -> np.ndarray:
    """Densidad de una normal unidimensional."""
    z = (x - media) / sigma
    return np.exp(-0.5 * z ** 2) / (sigma * np.sqrt(2.0 * np.pi))


def umbral_map_binario(a: float, sigma2: float, p_mas: float, p_menos: float) -> float:
    """Umbral MAP para símbolos antipodales ±a en AWGN."""
    return float((sigma2 / (2.0 * a)) * np.log(p_menos / p_mas))


def detectar_bits(rx: np.ndarray, umbral: float) -> np.ndarray:
    """Decisor binario a partir de un umbral."""
    return (rx >= umbral).astype(int)


def demo_deteccion(rng: np.random.Generator) -> list[Path]:
    """Genera figuras de ML/MAP y BER para detección óptima."""
    rutas = []
    a = 1.0
    sigma2 = 0.25
    sigma = np.sqrt(sigma2)
    p_mas = 0.8
    p_menos = 0.2
    tau_ml = 0.0
    tau_map = umbral_map_binario(a, sigma2, p_mas, p_menos)

    r = np.linspace(-3.0, 3.0, 800)
    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    ax.plot(r, pdf_normal(r, +a, sigma), lw=2.2, label="p(r|+A)")
    ax.plot(r, pdf_normal(r, -a, sigma), lw=2.2, label="p(r|-A)")
    ax.axvline(tau_ml, color="black", ls="--", lw=1.7, label="Umbral ML")
    ax.axvline(tau_map, color="crimson", ls=":", lw=2.2, label=f"Umbral MAP = {tau_map:.3f}")
    ax.fill_between(r, 0, pdf_normal(r, +a, sigma), where=r < tau_map, color="tab:blue", alpha=0.15)
    ax.fill_between(r, 0, pdf_normal(r, -a, sigma), where=r > tau_map, color="tab:orange", alpha=0.15)
    ax.set_title("Regiones de decisión ML y MAP para señales antipodales")
    ax.set_xlabel("Variable de decisión r")
    ax.set_ylabel("Densidad de probabilidad")
    ax.legend()
    rutas.append(guardar_figura(fig, "unidad2_deteccion_ml_map.png"))

    priors = np.linspace(0.05, 0.95, 400)
    umbrales = [umbral_map_binario(a, sigma2, p1, 1 - p1) for p1 in priors]
    fig, ax = plt.subplots(figsize=(7.5, 4.6))
    ax.plot(priors, umbrales, lw=2, color="tab:red")
    ax.axhline(0.0, color="black", ls="--", lw=1.3)
    ax.set_title("Efecto de las probabilidades a priori sobre el umbral MAP")
    ax.set_xlabel("P(+A)")
    ax.set_ylabel("Umbral óptimo τ")
    rutas.append(guardar_figura(fig, "unidad2_deteccion_umbral_priori.png"))

    ebn0_db = np.arange(0.0, 11.0, 1.0)
    ebn0_lin = 10 ** (ebn0_db / 10.0)
    ber_teo = qfunc(np.sqrt(2.0 * ebn0_lin))

    n_bits = 120000
    bits = rng.integers(0, 2, size=n_bits)
    simbolos = 2 * bits - 1
    ber_sim = []
    for gamma in ebn0_lin:
        sigma_mc = np.sqrt(1.0 / (2.0 * gamma))
        ruido = rng.normal(0.0, sigma_mc, size=n_bits)
        rx = simbolos + ruido
        bits_hat = detectar_bits(rx, 0.0)
        ber_sim.append(np.mean(bits_hat != bits))
    ber_sim = np.array(ber_sim)

    fig, ax = plt.subplots(figsize=(7.6, 4.8))
    ax.semilogy(ebn0_db, ber_teo, "o-", lw=2, label="BPSK óptimo teórico")
    ax.semilogy(ebn0_db, ber_sim, "s--", lw=1.8, label="Monte Carlo")
    ax.set_title("BER vs Eb/N0 para detección óptima en AWGN")
    ax.set_xlabel("Eb/N0 [dB]")
    ax.set_ylabel("BER")
    ax.legend()
    routes = guardar_figura(fig, "unidad2_deteccion_ber_vs_snr.png")
    rutas.append(routes)

    return rutas


# =========================
# Información semántica
# =========================
def contenido_bar_hillel_carnap(mundos_favorables: int, total_mundos: int) -> float:
    """Contenido lógico -log2(m/N)."""
    if mundos_favorables <= 0:
        return np.inf
    return float(np.log2(total_mundos / mundos_favorables))


def informacion_semantica_fuerte(prob_logica: float, verdadero: bool) -> float:
    """Versión pedagógica de información semántica fuerte."""
    if (not verdadero) or prob_logica <= 0:
        return 0.0
    return float(-np.log2(prob_logica))


def demo_informacion_semantica() -> list[Path]:
    """Genera comparaciones entre métricas sintácticas y semánticas."""
    rutas = []

    simbolos = np.array([0.4, 0.3, 0.2, 0.1])
    significados = np.array([0.7, 0.2, 0.1])
    hs = entropy(simbolos)
    hsem = entropy(significados)

    fig, axes = plt.subplots(1, 2, figsize=(10.5, 4.5))
    axes[0].bar(["x1", "x2", "x3", "x4"], simbolos, color="tab:blue")
    axes[0].set_ylim(0, 0.8)
    axes[0].set_title(f"Entropía de Shannon\nH(X) = {hs:.3f} bits")
    axes[0].set_ylabel("Probabilidad")
    axes[1].bar(["m1", "m2", "m3"], significados, color="tab:green")
    axes[1].set_ylim(0, 0.8)
    axes[1].set_title(f"Entropía semántica\nH_S(M) = {hsem:.3f} bits")
    axes[1].set_ylabel("Probabilidad")
    rutas.append(guardar_figura(fig, "unidad2_semantica_entropia_vs_semantica.png"))

    total_mundos = 8
    mensajes = [
        {"nombre": "Estado normal", "p_simbolo": 0.60, "m": 6, "verdadero": True},
        {"nombre": "Fallo sensor 1", "p_simbolo": 0.12, "m": 2, "verdadero": True},
        {"nombre": "Sobrecarga crítica", "p_simbolo": 0.08, "m": 1, "verdadero": True},
        {"nombre": "Diagnóstico contradictorio", "p_simbolo": 0.20, "m": 0, "verdadero": False},
    ]

    nombres = [m["nombre"] for m in mensajes]
    sorpresa_shannon = [-np.log2(m["p_simbolo"]) for m in mensajes]
    contenido_logico = [contenido_bar_hillel_carnap(m["m"], total_mundos) for m in mensajes]
    contenido_fuerte = [
        informacion_semantica_fuerte(m["m"] / total_mundos if m["m"] > 0 else 0.0, m["verdadero"])
        for m in mensajes
    ]
    contenido_plot = [np.nan if np.isinf(v) else v for v in contenido_logico]

    x = np.arange(len(nombres))
    w = 0.25
    fig, ax = plt.subplots(figsize=(11, 5.4))
    ax.bar(x - w, sorpresa_shannon, width=w, label="Sorpresa de Shannon")
    ax.bar(x, contenido_plot, width=w, label="Contenido Bar-Hillel-Carnap")
    ax.bar(x + w, contenido_fuerte, width=w, label="Contenido semántico fuerte")
    ax.set_xticks(x)
    ax.set_xticklabels(nombres, rotation=12)
    ax.set_ylabel("Bits")
    ax.set_title("Comparación entre métricas sintácticas y semánticas")
    ax.legend(fontsize=8)
    for i, valor in enumerate(contenido_logico):
        if np.isinf(valor):
            ax.text(i, max(sorpresa_shannon) + 0.35, "∞ lógica\n0 fuerte", ha="center", color="crimson")
    rutas.append(guardar_figura(fig, "unidad2_semantica_metricas_comparadas.png"))

    return rutas


# =========================
# Orquestación
# =========================
def ejecutar_secciones(secciones: list[str], semilla: int) -> list[Path]:
    """Ejecuta las secciones seleccionadas y devuelve las figuras generadas."""
    configurar_estilo()
    asegurar_directorios()
    rng = np.random.default_rng(semilla)
    rutas: list[Path] = []

    if "informacion" in secciones:
        rutas.extend(demo_medidas_informacion(rng))
    if "pcm" in secciones:
        rutas.extend(demo_pcm())
    if "capacidad" in secciones:
        rutas.extend(demo_capacidad_canal())
    if "deteccion" in secciones:
        rutas.extend(demo_deteccion(rng))
    if "semantica" in secciones:
        rutas.extend(demo_informacion_semantica())

    return rutas


def parse_args() -> argparse.Namespace:
    """Parsea argumentos de línea de comandos."""
    parser = argparse.ArgumentParser(
        description="Simulador integral de la Unidad 2: teoría de información, PCM, capacidad, detección y semántica."
    )
    parser.add_argument(
        "--secciones",
        nargs="+",
        default=["todas"],
        choices=["todas", "informacion", "pcm", "capacidad", "deteccion", "semantica"],
        help="Secciones a ejecutar.",
    )
    parser.add_argument("--semilla", type=int, default=42, help="Semilla del generador aleatorio.")
    return parser.parse_args()


def normalizar_secciones(secciones: list[str]) -> list[str]:
    """Expande la opción 'todas' a la lista completa."""
    if "todas" in secciones:
        return ["informacion", "pcm", "capacidad", "deteccion", "semantica"]
    return secciones


def main() -> None:
    """Punto de entrada principal."""
    args = parse_args()
    secciones = normalizar_secciones(args.secciones)
    rutas = ejecutar_secciones(secciones, semilla=args.semilla)

    print("Simulación Unidad 2 completada.")
    print(f"Secciones ejecutadas: {', '.join(secciones)}")
    print(f"Figuras generadas en: {FIG_DIR}")
    for ruta in rutas:
        print(f" - {ruta.name}")


if __name__ == "__main__":
    main()
