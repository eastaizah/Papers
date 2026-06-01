#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Simulaciones de la Unidad 1: Comunicaciones digitales en banda base."""

import argparse
import os

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.special import erfc


# -----------------------------------------------------------------------------
# Utilidades generales
# -----------------------------------------------------------------------------

def guardar_figura(figura, carpeta_figuras, nombre_archivo):
    """Guarda una figura y libera memoria."""
    os.makedirs(carpeta_figuras, exist_ok=True)
    ruta = os.path.join(carpeta_figuras, nombre_archivo)
    figura.tight_layout()
    figura.savefig(ruta, dpi=200, bbox_inches="tight")
    plt.close(figura)
    print(f"[OK] Figura guardada en: {ruta}")


def pulso_rectangular(t, T=1.0):
    """Pulso rectangular unitario centrado en cero."""
    return np.where(np.abs(t) <= T / 2.0, 1.0, 0.0)



def pulso_coseno_alzado(t, T=1.0, beta=0.35):
    """Respuesta temporal de un pulso raised cosine normalizado."""
    tau = np.asarray(t, dtype=float) / T
    if np.isclose(beta, 0.0):
        return np.sinc(tau)

    numerador = np.sinc(tau) * np.cos(np.pi * beta * tau)
    denominador = 1.0 - (2.0 * beta * tau) ** 2
    h = np.empty_like(tau)

    mascara_regular = ~np.isclose(denominador, 0.0)
    h[mascara_regular] = numerador[mascara_regular] / denominador[mascara_regular]

    # Límite analítico en t = ±T/(2 beta).
    h[~mascara_regular] = (np.pi / 4.0) * np.sinc(1.0 / (2.0 * beta))
    return h



def pulso_rrc(t, T=1.0, beta=0.35):
    """Respuesta temporal de un pulso root raised cosine."""
    tau = np.asarray(t, dtype=float) / T

    if np.isclose(beta, 0.0):
        return np.sinc(tau)

    h = np.zeros_like(tau)
    mascara_cero = np.isclose(tau, 0.0)
    mascara_singular = np.isclose(np.abs(tau), 1.0 / (4.0 * beta))
    mascara_regular = ~(mascara_cero | mascara_singular)

    h[mascara_cero] = 1.0 + beta * (4.0 / np.pi - 1.0)

    termino_1 = (1.0 + 2.0 / np.pi) * np.sin(np.pi / (4.0 * beta))
    termino_2 = (1.0 - 2.0 / np.pi) * np.cos(np.pi / (4.0 * beta))
    h[mascara_singular] = (beta / np.sqrt(2.0)) * (termino_1 + termino_2)

    tau_r = tau[mascara_regular]
    numerador = (
        np.sin(np.pi * tau_r * (1.0 - beta))
        + 4.0 * beta * tau_r * np.cos(np.pi * tau_r * (1.0 + beta))
    )
    denominador = np.pi * tau_r * (1.0 - (4.0 * beta * tau_r) ** 2)
    h[mascara_regular] = numerador / denominador
    return h



def normalizar_energia_discreta(h):
    """Normaliza un filtro para que su energía discreta sea unitaria."""
    energia = np.sum(np.abs(h) ** 2)
    return h / np.sqrt(energia)



def calcular_fft(x, dt):
    """Calcula la transformada de Fourier continua aproximada mediante FFT."""
    x = np.asarray(x)
    X = np.fft.fftshift(np.fft.fft(np.fft.ifftshift(x))) * dt
    f = np.fft.fftshift(np.fft.fftfreq(len(x), d=dt))
    return f, X



def estimar_psd(x, fs):
    """Estima la PSD con el método de Welch."""
    nperseg = min(1024, len(x))
    f, pxx = signal.welch(
        x,
        fs=fs,
        nperseg=nperseg,
        return_onesided=False,
        scaling="density",
    )
    return np.fft.fftshift(f), np.fft.fftshift(pxx)



def interpolacion_sinc(t_objetivo, t_muestras, x_muestras):
    """Reconstrucción ideal aproximada mediante interpolación sinc."""
    Ts = t_muestras[1] - t_muestras[0]
    matriz = np.sinc((t_objetivo[:, None] - t_muestras[None, :]) / Ts)
    return matriz @ x_muestras



def aplicar_filtro_pasabajos_fft(x, fs, ancho_banda):
    """Aplica un pasabajos ideal usando una máscara en frecuencia."""
    X = np.fft.fft(x)
    frecuencias = np.fft.fftfreq(len(x), d=1.0 / fs)
    mascara = np.abs(frecuencias) <= ancho_banda
    return np.real(np.fft.ifft(X * mascara))



def generar_senal_banda_base(simbolos, sps, pulso):
    """Convierte una secuencia de símbolos en una forma de onda muestreada."""
    sobremuestreada = np.zeros(len(simbolos) * sps)
    sobremuestreada[::sps] = simbolos
    return np.convolve(sobremuestreada, pulso, mode="full")



def codificar_nrz(bits, sps):
    """Codificación NRZ polar."""
    niveles = 2 * bits - 1
    return np.repeat(niveles, sps)



def codificar_rz(bits, sps):
    """Codificación RZ polar."""
    niveles = 2 * bits - 1
    senal = np.zeros(len(bits) * sps)
    mitad = sps // 2
    for i, nivel in enumerate(niveles):
        inicio = i * sps
        senal[inicio:inicio + mitad] = nivel
    return senal



def codificar_manchester(bits, sps):
    """Codificación Manchester polar."""
    senal = np.zeros(len(bits) * sps)
    mitad = sps // 2
    for i, bit in enumerate(bits):
        inicio = i * sps
        if bit == 1:
            senal[inicio:inicio + mitad] = 1.0
            senal[inicio + mitad:(i + 1) * sps] = -1.0
        else:
            senal[inicio:inicio + mitad] = -1.0
            senal[inicio + mitad:(i + 1) * sps] = 1.0
    return senal



def graficar_ojo(ax, senal, sps, titulo, num_trazas=80, desplazamiento=0):
    """Dibuja un diagrama de ojo de dos intervalos de símbolo."""
    ventana = 2 * sps
    tiempo = np.arange(ventana) / sps
    max_trazas = min(num_trazas, max((len(senal) - desplazamiento - ventana) // sps, 1))

    for k in range(max_trazas):
        inicio = desplazamiento + k * sps
        segmento = senal[inicio:inicio + ventana]
        if len(segmento) == ventana:
            ax.plot(tiempo, segmento, color="tab:blue", alpha=0.18, linewidth=0.8)

    ax.set_title(titulo)
    ax.set_xlabel("Tiempo [T_símbolo]")
    ax.set_ylabel("Amplitud")
    ax.grid(True, alpha=0.3)



def simular_enlace_banda_base(num_bits, sps, span, beta, snr_db, semilla=1234, ancho_banda_canal=None):
    """Simula la cadena Tx-Canal-Rx con conformación RRC y detección binaria."""
    generador = np.random.default_rng(semilla)
    bits = generador.integers(0, 2, num_bits)
    simbolos = 2 * bits - 1

    tiempo_pulso = np.arange(-span * sps, span * sps + 1) / sps
    h_rrc = normalizar_energia_discreta(pulso_rrc(tiempo_pulso, T=1.0, beta=beta))

    tx = generar_senal_banda_base(simbolos, sps, h_rrc)

    if ancho_banda_canal is not None:
        tx_canal = aplicar_filtro_pasabajos_fft(tx, fs=sps, ancho_banda=ancho_banda_canal)
    else:
        tx_canal = tx.copy()

    ebn0 = 10 ** (snr_db / 10.0)
    sigma = np.sqrt(1.0 / (2.0 * ebn0))
    ruido = sigma * generador.standard_normal(len(tx_canal))
    rx = tx_canal + ruido

    salida_mf = np.convolve(rx, h_rrc[::-1], mode="full")
    retardo_total = len(h_rrc) - 1
    indices_muestreo = retardo_total + np.arange(num_bits) * sps
    muestras = salida_mf[indices_muestreo]
    bits_estimados = (muestras >= 0).astype(int)
    ber = np.mean(bits != bits_estimados)

    return {
        "bits": bits,
        "simbolos": simbolos,
        "h_rrc": h_rrc,
        "tx": tx,
        "tx_canal": tx_canal,
        "ruido": ruido,
        "rx": rx,
        "salida_mf": salida_mf,
        "indices_muestreo": indices_muestreo,
        "muestras": muestras,
        "bits_estimados": bits_estimados,
        "ber": ber,
        "sigma": sigma,
    }


# -----------------------------------------------------------------------------
# 1) Señales, Fourier, PSD, Parseval y aliasing
# -----------------------------------------------------------------------------

def simular_senales_y_fourier(carpeta_figuras, rolloff):
    """Genera pulsos baseband y estudia sus propiedades espectrales."""
    t = np.linspace(-4.0, 4.0, 4096, endpoint=False)
    dt = t[1] - t[0]
    fs = 1.0 / dt

    senales = {
        "Rectangular": pulso_rectangular(t, T=1.0),
        "Sinc": np.sinc(t),
        "Coseno alzado": pulso_coseno_alzado(t, T=1.0, beta=rolloff),
    }

    figura, ejes = plt.subplots(3, 3, figsize=(15, 10))
    energias_tiempo = []
    energias_frecuencia = []
    nombres = []

    for fila, (nombre, x) in enumerate(senales.items()):
        f, X = calcular_fft(x, dt)
        f_psd, pxx = estimar_psd(x, fs)
        df = f[1] - f[0]
        energia_t = np.sum(np.abs(x) ** 2) * dt
        energia_f = np.sum(np.abs(X) ** 2) * df

        energias_tiempo.append(energia_t)
        energias_frecuencia.append(energia_f)
        nombres.append(nombre)

        ejes[fila, 0].plot(t, x, color="tab:blue")
        ejes[fila, 0].set_title(f"{nombre} en tiempo")
        ejes[fila, 0].set_xlabel("Tiempo")
        ejes[fila, 0].set_ylabel("Amplitud")
        ejes[fila, 0].grid(True, alpha=0.3)

        ejes[fila, 1].plot(f, np.abs(X), color="tab:orange")
        ejes[fila, 1].set_xlim(-5, 5)
        ejes[fila, 1].set_title(f"|X(f)| de {nombre}")
        ejes[fila, 1].set_xlabel("Frecuencia [Hz]")
        ejes[fila, 1].set_ylabel("Magnitud")
        ejes[fila, 1].grid(True, alpha=0.3)

        ejes[fila, 2].semilogy(f_psd, np.maximum(pxx, 1e-12), color="tab:green")
        ejes[fila, 2].set_xlim(-5, 5)
        ejes[fila, 2].set_title(f"PSD estimada de {nombre}")
        ejes[fila, 2].set_xlabel("Frecuencia [Hz]")
        ejes[fila, 2].set_ylabel("PSD")
        ejes[fila, 2].grid(True, alpha=0.3)

    guardar_figura(figura, carpeta_figuras, "01_senales_fourier_psd.png")

    errores_relativos = np.abs(np.array(energias_tiempo) - np.array(energias_frecuencia)) / np.maximum(1e-12, energias_tiempo)
    figura, ejes = plt.subplots(1, 2, figsize=(12, 4))
    posiciones = np.arange(len(nombres))
    ancho = 0.35

    ejes[0].bar(posiciones - ancho / 2, energias_tiempo, width=ancho, label="Tiempo")
    ejes[0].bar(posiciones + ancho / 2, energias_frecuencia, width=ancho, label="Frecuencia")
    ejes[0].set_xticks(posiciones)
    ejes[0].set_xticklabels(nombres, rotation=10)
    ejes[0].set_ylabel("Energía")
    ejes[0].set_title("Verificación numérica de Parseval")
    ejes[0].legend()
    ejes[0].grid(True, axis="y", alpha=0.3)

    ejes[1].bar(posiciones, errores_relativos, color="tab:red")
    ejes[1].set_xticks(posiciones)
    ejes[1].set_xticklabels(nombres, rotation=10)
    ejes[1].set_ylabel("Error relativo")
    ejes[1].set_title("Error numérico de Parseval")
    ejes[1].grid(True, axis="y", alpha=0.3)

    guardar_figura(figura, carpeta_figuras, "02_parseval.png")

    for nombre, et, ef, err in zip(nombres, energias_tiempo, energias_frecuencia, errores_relativos):
        print(f"[Parseval] {nombre}: E_tiempo={et:.6f}, E_freq={ef:.6f}, error={err:.3e}")



def simular_aliasing(carpeta_figuras):
    """Demuestra aliasing al muestrear una señal por debajo de Nyquist."""
    f1 = 3.0
    f2 = 11.0
    duracion = 1.0
    t_cont = np.linspace(0.0, duracion, 4000, endpoint=False)
    x_cont = np.cos(2.0 * np.pi * f1 * t_cont) + 0.7 * np.cos(2.0 * np.pi * f2 * t_cont)

    frecuencias_muestreo = [40.0, 16.0]
    etiquetas = ["Sin aliasing (fs=40 Hz)", "Con aliasing (fs=16 Hz)"]

    figura, ejes = plt.subplots(2, 2, figsize=(14, 8))

    for fila, (fs, etiqueta) in enumerate(zip(frecuencias_muestreo, etiquetas)):
        t_m = np.arange(0.0, duracion, 1.0 / fs)
        x_m = np.cos(2.0 * np.pi * f1 * t_m) + 0.7 * np.cos(2.0 * np.pi * f2 * t_m)
        x_rec = interpolacion_sinc(t_cont, t_m, x_m)

        nfft = 2048
        espectro = np.fft.fftshift(np.fft.fft(x_m, n=nfft))
        frec = np.fft.fftshift(np.fft.fftfreq(nfft, d=1.0 / fs))

        ejes[fila, 0].plot(t_cont, x_cont, label="Señal original", linewidth=1.5)
        ejes[fila, 0].plot(t_cont, x_rec, "--", label="Reconstrucción sinc", linewidth=1.2)
        ejes[fila, 0].stem(t_m, x_m, linefmt="tab:red", markerfmt="ro", basefmt=" ")
        ejes[fila, 0].set_title(etiqueta)
        ejes[fila, 0].set_xlabel("Tiempo [s]")
        ejes[fila, 0].set_ylabel("Amplitud")
        ejes[fila, 0].set_xlim(0.0, 0.5)
        ejes[fila, 0].grid(True, alpha=0.3)
        if fila == 0:
            ejes[fila, 0].legend(loc="upper right")

        ejes[fila, 1].plot(frec, np.abs(espectro), color="tab:purple")
        ejes[fila, 1].set_xlim(-fs / 2.0, fs / 2.0)
        ejes[fila, 1].set_title(f"Espectro discreto para fs={fs:.0f} Hz")
        ejes[fila, 1].set_xlabel("Frecuencia [Hz]")
        ejes[fila, 1].set_ylabel("|X(f)|")
        ejes[fila, 1].grid(True, alpha=0.3)

    guardar_figura(figura, carpeta_figuras, "03_aliasing.png")


# -----------------------------------------------------------------------------
# 2) Conformación de pulsos, códigos de línea, ojo e ISI
# -----------------------------------------------------------------------------

def simular_codigos_de_linea(carpeta_figuras):
    """Compara códigos NRZ, RZ y Manchester."""
    bits = np.array([1, 0, 1, 1, 0, 0, 1, 0])
    sps = 40
    t = np.arange(len(bits) * sps) / sps

    senales = {
        "NRZ polar": codificar_nrz(bits, sps),
        "RZ polar": codificar_rz(bits, sps),
        "Manchester": codificar_manchester(bits, sps),
    }

    figura, ejes = plt.subplots(3, 1, figsize=(14, 7), sharex=True)
    for ax, (nombre, senal) in zip(ejes, senales.items()):
        ax.plot(t, senal, linewidth=2.0)
        for k in range(len(bits) + 1):
            ax.axvline(k, color="gray", alpha=0.2, linewidth=0.8)
        ax.set_title(f"Código de línea: {nombre}")
        ax.set_ylabel("Amplitud")
        ax.set_ylim(-1.4, 1.4)
        ax.grid(True, alpha=0.3)

    ejes[-1].set_xlabel("Tiempo [intervalos de bit]")
    guardar_figura(figura, carpeta_figuras, "04_codigos_linea.png")



def simular_pulse_shaping(carpeta_figuras, rolloff):
    """Estudia RC/RRC, diagramas de ojo e ISI por truncamiento."""
    sps = 32
    span = 8
    betas = [0.1, rolloff, 0.9]
    tiempo = np.arange(-span * sps, span * sps + 1) / sps

    figura, ejes = plt.subplots(2, 2, figsize=(14, 10))
    for beta in betas:
        h_rc = pulso_coseno_alzado(tiempo, T=1.0, beta=beta)
        h_rrc = normalizar_energia_discreta(pulso_rrc(tiempo, T=1.0, beta=beta))

        ejes[0, 0].plot(tiempo, h_rc, label=fr"RC $\beta={beta:.2f}$")
        ejes[0, 1].plot(tiempo, h_rrc, label=fr"RRC $\beta={beta:.2f}$")

        f_rc, H_rc = calcular_fft(h_rc, 1.0 / sps)
        f_rrc, H_rrc = calcular_fft(h_rrc, 1.0 / sps)
        ejes[1, 0].plot(f_rc, np.abs(H_rc), label=fr"RC $\beta={beta:.2f}$")
        ejes[1, 1].plot(f_rrc, np.abs(H_rrc), label=fr"RRC $\beta={beta:.2f}$")

    ejes[0, 0].set_title("Pulsos coseno alzado en tiempo")
    ejes[0, 1].set_title("Pulsos raíz coseno alzado en tiempo")
    ejes[1, 0].set_title("Magnitud espectral RC")
    ejes[1, 1].set_title("Magnitud espectral RRC")

    for ax in ejes.ravel():
        ax.grid(True, alpha=0.3)
        ax.legend()
    for ax in ejes[1, :]:
        ax.set_xlim(-2.0, 2.0)
        ax.set_xlabel("Frecuencia [ciclos/símbolo]")
    for ax in ejes[0, :]:
        ax.set_xlabel("Tiempo [símbolos]")
        ax.set_ylabel("Amplitud")
    for ax in ejes[1, :]:
        ax.set_ylabel("Magnitud")

    guardar_figura(figura, carpeta_figuras, "05_pulse_shaping_rc_rrc.png")

    # Se usa una secuencia pseudoaleatoria para mostrar el cierre/apertura del ojo.
    rng = np.random.default_rng(2024)
    simbolos = 2 * rng.integers(0, 2, 300) - 1
    figura, ejes = plt.subplots(1, 3, figsize=(15, 4.5), sharey=True)

    for ax, beta in zip(ejes, betas):
        h_rrc = normalizar_energia_discreta(pulso_rrc(tiempo, T=1.0, beta=beta))
        tx = generar_senal_banda_base(simbolos, sps, h_rrc)
        rx_mf = np.convolve(tx, h_rrc[::-1], mode="full")
        desplazamiento = len(h_rrc) - 1 + 10 * sps
        graficar_ojo(ax, rx_mf, sps, titulo=fr"Ojo con $\beta={beta:.2f}$", desplazamiento=desplazamiento)

    guardar_figura(figura, carpeta_figuras, "06_diagramas_ojo.png")

    # La ISI residual aparece por la truncación finita del filtro, más notable para beta pequeño.
    figura, ax = plt.subplots(figsize=(10, 5))
    desplazamientos = np.arange(-6, 7)
    for beta in betas:
        h_rrc = normalizar_energia_discreta(pulso_rrc(tiempo, T=1.0, beta=beta))
        respuesta_total = np.convolve(h_rrc, h_rrc[::-1], mode="full")
        centro = len(respuesta_total) // 2
        muestras = respuesta_total[centro + desplazamientos * sps]
        ax.plot(desplazamientos, muestras, marker="o", label=fr"$\beta={beta:.2f}$")
        isi = np.sum(np.abs(muestras[desplazamientos != 0]))
        print(f"[ISI] beta={beta:.2f} -> suma residual |ISI|={isi:.4e}")

    ax.axhline(0.0, color="black", linewidth=0.8)
    ax.set_title("Muestras de la respuesta global en instantes de símbolo")
    ax.set_xlabel("Desplazamiento [símbolos]")
    ax.set_ylabel("Amplitud muestreada")
    ax.grid(True, alpha=0.3)
    ax.legend()
    guardar_figura(figura, carpeta_figuras, "07_isi_rolloff.png")


# -----------------------------------------------------------------------------
# 3) Cadena completa Tx-CH-Rx y BER
# -----------------------------------------------------------------------------

def simular_cadena_tx_ch_rx(carpeta_figuras, snr_min, snr_max, num_bits, rolloff):
    """Ejecuta la cadena completa Tx-Canal-Rx y calcula BER."""
    sps = 16
    span = 8
    snr_referencia = 0.5 * (snr_min + snr_max)
    resultado = simular_enlace_banda_base(
        num_bits=max(400, min(num_bits, 1200)),
        sps=sps,
        span=span,
        beta=rolloff,
        snr_db=snr_referencia,
        semilla=77,
    )

    num_mostrar = 12
    tiempo_tx = np.arange(len(resultado["tx"])) / sps
    tiempo_rx = np.arange(len(resultado["rx"])) / sps
    tiempo_mf = np.arange(len(resultado["salida_mf"])) / sps

    figura, ejes = plt.subplots(4, 1, figsize=(14, 10), sharex=False)

    ejes[0].step(np.arange(num_mostrar), resultado["bits"][:num_mostrar], where="post")
    ejes[0].set_ylim(-0.2, 1.2)
    ejes[0].set_title("Bits transmitidos")
    ejes[0].set_ylabel("Bit")
    ejes[0].grid(True, alpha=0.3)

    mascara_tx = tiempo_tx <= num_mostrar
    ejes[1].plot(tiempo_tx[mascara_tx], resultado["tx"][mascara_tx], color="tab:blue")
    ejes[1].set_title(f"Señal conformada RRC (β={rolloff:.2f})")
    ejes[1].set_ylabel("Amplitud")
    ejes[1].grid(True, alpha=0.3)

    mascara_rx = tiempo_rx <= num_mostrar
    ejes[2].plot(tiempo_rx[mascara_rx], resultado["rx"][mascara_rx], color="tab:red")
    ejes[2].set_title(f"Salida del canal AWGN (SNR={snr_referencia:.1f} dB)")
    ejes[2].set_ylabel("Amplitud")
    ejes[2].grid(True, alpha=0.3)

    mascara_mf = tiempo_mf <= num_mostrar + 2 * span
    ejes[3].plot(tiempo_mf[mascara_mf], resultado["salida_mf"][mascara_mf], color="tab:green")
    tiempos_muestreo = resultado["indices_muestreo"] / sps
    mascara_muestras = tiempos_muestreo <= num_mostrar
    ejes[3].plot(
        tiempos_muestreo[mascara_muestras],
        resultado["muestras"][mascara_muestras],
        "ko",
        label="Instantes de decisión",
    )
    ejes[3].axhline(0.0, color="black", linewidth=0.8)
    ejes[3].set_title("Salida del filtro casado y muestras de detección")
    ejes[3].set_ylabel("Amplitud")
    ejes[3].set_xlabel("Tiempo [símbolos]")
    ejes[3].grid(True, alpha=0.3)
    ejes[3].legend()

    guardar_figura(figura, carpeta_figuras, "08_cadena_tx_ch_rx.png")

    snrs_db = np.arange(int(np.floor(snr_min)), int(np.ceil(snr_max)) + 1)
    bers = []
    for i, snr_db in enumerate(snrs_db):
        resultado_snr = simular_enlace_banda_base(
            num_bits=num_bits,
            sps=sps,
            span=span,
            beta=rolloff,
            snr_db=float(snr_db),
            semilla=100 + i,
        )
        bers.append(resultado_snr["ber"])
        print(f"[BER] SNR={snr_db:>2} dB -> BER simulada={resultado_snr['ber']:.6f}")

    bers = np.array(bers)
    ber_teorica = 0.5 * erfc(np.sqrt(10 ** (snrs_db / 10.0)))

    figura, ax = plt.subplots(figsize=(8, 5))
    ax.semilogy(snrs_db, np.maximum(bers, 1e-6), "o-", label="Simulada")
    ax.semilogy(snrs_db, np.maximum(ber_teorica, 1e-9), "--", label="BPSK teórica")
    ax.set_title("BER vs SNR en cadena banda base con RRC + filtro casado")
    ax.set_xlabel("SNR / EbN0 [dB]")
    ax.set_ylabel("BER")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend()
    guardar_figura(figura, carpeta_figuras, "09_ber_vs_snr.png")


# -----------------------------------------------------------------------------
# 4) Efectos de parámetros: ancho de banda, muestreo y rolloff
# -----------------------------------------------------------------------------

def simular_efectos_parametros(carpeta_figuras, rolloff):
    """Resume el efecto de parámetros clave sobre calidad e ISI."""
    sps = 16
    span = 8
    num_bits = 2500

    # Efecto del ancho de banda del canal sobre la BER.
    anchos_banda = np.array([0.25, 0.35, 0.50, 0.75, 1.00])
    bers_bw = []
    for i, bw in enumerate(anchos_banda):
        resultado = simular_enlace_banda_base(
            num_bits=num_bits,
            sps=sps,
            span=span,
            beta=rolloff,
            snr_db=12.0,
            semilla=300 + i,
            ancho_banda_canal=float(bw),
        )
        bers_bw.append(resultado["ber"])

    # Efecto de la tasa de muestreo sobre la reconstrucción sinc.
    t_ref = np.linspace(0.0, 1.0, 4000, endpoint=False)
    x_ref = np.sinc(6.0 * (t_ref - 0.5))
    fs_list = np.array([8.0, 16.0, 32.0, 64.0])
    errores_reconstruccion = []

    figura_recon, ejes_recon = plt.subplots(2, 2, figsize=(12, 8), sharex=True, sharey=True)
    for ax, fs in zip(ejes_recon.ravel(), fs_list):
        t_m = np.arange(0.0, 1.0, 1.0 / fs)
        x_m = np.sinc(6.0 * (t_m - 0.5))
        x_rec = interpolacion_sinc(t_ref, t_m, x_m)
        mse = np.mean((x_ref - x_rec) ** 2)
        errores_reconstruccion.append(mse)

        ax.plot(t_ref, x_ref, label="Original", linewidth=1.5)
        ax.plot(t_ref, x_rec, "--", label="Reconstruida", linewidth=1.2)
        ax.stem(t_m, x_m, linefmt="tab:red", markerfmt="ro", basefmt=" ")
        ax.set_title(f"fs={fs:.0f} Hz, MSE={mse:.2e}")
        ax.grid(True, alpha=0.3)

    ejes_recon[0, 0].legend(loc="upper right")
    for ax in ejes_recon[-1, :]:
        ax.set_xlabel("Tiempo [s]")
    for ax in ejes_recon[:, 0]:
        ax.set_ylabel("Amplitud")
    guardar_figura(figura_recon, carpeta_figuras, "10_reconstruccion_muestreo.png")

    # Efecto del rolloff sobre ISI residual por truncamiento del filtro.
    betas = np.linspace(0.05, 1.0, 10)
    isi_residual = []
    tiempo = np.arange(-span * sps, span * sps + 1) / sps
    desplazamientos = np.arange(-8, 9)
    for beta in betas:
        h_rrc = normalizar_energia_discreta(pulso_rrc(tiempo, T=1.0, beta=float(beta)))
        respuesta_total = np.convolve(h_rrc, h_rrc[::-1], mode="full")
        centro = len(respuesta_total) // 2
        muestras = respuesta_total[centro + desplazamientos * sps]
        isi = np.sum(np.abs(muestras[desplazamientos != 0]))
        isi_residual.append(isi)

    figura, ejes = plt.subplots(1, 3, figsize=(16, 4.5))

    ejes[0].semilogy(anchos_banda, np.maximum(bers_bw, 1e-6), "o-", color="tab:blue")
    ejes[0].set_title("Ancho de banda del canal vs BER")
    ejes[0].set_xlabel("Ancho de banda [ciclos/símbolo]")
    ejes[0].set_ylabel("BER a 12 dB")
    ejes[0].grid(True, which="both", alpha=0.3)

    ejes[1].semilogy(fs_list, np.maximum(errores_reconstruccion, 1e-12), "s-", color="tab:orange")
    ejes[1].set_title("Frecuencia de muestreo vs error")
    ejes[1].set_xlabel("fs [Hz]")
    ejes[1].set_ylabel("MSE de reconstrucción")
    ejes[1].grid(True, which="both", alpha=0.3)

    ejes[2].plot(betas, isi_residual, "^-", color="tab:green")
    ejes[2].set_title("Rolloff vs ISI residual")
    ejes[2].set_xlabel("Factor de rolloff β")
    ejes[2].set_ylabel("Suma |ISI| fuera del pico")
    ejes[2].grid(True, alpha=0.3)

    guardar_figura(figura, carpeta_figuras, "11_efectos_parametros.png")

    for bw, ber in zip(anchos_banda, bers_bw):
        print(f"[BW] B={bw:.2f} -> BER={ber:.6f}")
    for fs, mse in zip(fs_list, errores_reconstruccion):
        print(f"[Muestreo] fs={fs:.0f} Hz -> MSE={mse:.6e}")


# -----------------------------------------------------------------------------
# Función principal
# -----------------------------------------------------------------------------

def main():
    """Ejecuta todas las demostraciones solicitadas."""
    parser = argparse.ArgumentParser(
        description="Simulaciones de la Unidad 1: Introducción a las comunicaciones digitales en banda base"
    )
    parser.add_argument("--snr_min", type=float, default=0.0, help="SNR mínima para la curva BER [dB]")
    parser.add_argument("--snr_max", type=float, default=10.0, help="SNR máxima para la curva BER [dB]")
    parser.add_argument("--num_bits", type=int, default=4000, help="Número de bits para la simulación BER")
    parser.add_argument("--rolloff", type=float, default=0.35, help="Factor de rolloff para RC/RRC")
    args = parser.parse_args()

    if args.num_bits < 100:
        raise ValueError("--num_bits debe ser al menos 100 para obtener una BER representativa.")
    if not (0.0 <= args.rolloff <= 1.0):
        raise ValueError("--rolloff debe pertenecer al intervalo [0, 1].")
    if args.snr_max < args.snr_min:
        raise ValueError("--snr_max debe ser mayor o igual que --snr_min.")

    directorio_script = os.path.dirname(os.path.abspath(__file__))
    carpeta_figuras = os.path.join(directorio_script, "figuras")
    os.makedirs(carpeta_figuras, exist_ok=True)

    print("Iniciando simulaciones de la Unidad 1...")
    simular_senales_y_fourier(carpeta_figuras, args.rolloff)
    simular_aliasing(carpeta_figuras)
    simular_codigos_de_linea(carpeta_figuras)
    simular_pulse_shaping(carpeta_figuras, args.rolloff)
    simular_cadena_tx_ch_rx(carpeta_figuras, args.snr_min, args.snr_max, args.num_bits, args.rolloff)
    simular_efectos_parametros(carpeta_figuras, args.rolloff)
    print("Simulaciones finalizadas correctamente.")


if __name__ == "__main__":
    main()
