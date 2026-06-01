#!/usr/bin/env python3
"""Simulaciones de la Unidad 4: Codificación de Canal."""
from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Sequence

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d
from scipy.special import erfc


# ==============================
# Utilidades generales
# ==============================


def asegurar_directorio(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


# ==============================
# Aritmética en GF(2) y GF(2^m)
# ==============================


def gf2_add_table() -> np.ndarray:
    return np.array([[0, 1], [1, 0]], dtype=np.uint8)



def gf2_mul_table() -> np.ndarray:
    return np.array([[0, 0], [0, 1]], dtype=np.uint8)



def gf_degree(poly: int) -> int:
    return poly.bit_length() - 1



def gf_multiply(a: int, b: int, m: int, prim_poly: int) -> int:
    """Multiplicación en GF(2^m) usando base polinomial."""
    result = 0
    mask = (1 << m) - 1
    aa = a
    bb = b
    while bb:
        if bb & 1:
            result ^= aa
        bb >>= 1
        aa <<= 1
        if aa & (1 << m):
            aa ^= prim_poly
    return result & mask



def gf_power(a: int, exp: int, m: int, prim_poly: int) -> int:
    if exp == 0:
        return 1
    result = 1
    base = a
    e = exp
    while e:
        if e & 1:
            result = gf_multiply(result, base, m, prim_poly)
        base = gf_multiply(base, base, m, prim_poly)
        e >>= 1
    return result



def gf_order(a: int, m: int, prim_poly: int) -> int:
    if a == 0:
        return 0
    q_minus_1 = (1 << m) - 1
    value = 1
    for order in range(1, q_minus_1 + 1):
        value = gf_multiply(value, a, m, prim_poly)
        if value == 1:
            return order
    return q_minus_1



def find_primitive_element(m: int, prim_poly: int) -> int:
    q = 1 << m
    for element in range(2, q):
        if gf_order(element, m, prim_poly) == q - 1:
            return element
    raise ValueError("No se encontró elemento primitivo.")



def build_log_tables(m: int, prim_poly: int, primitive: int) -> tuple[np.ndarray, dict[int, int]]:
    q = 1 << m
    power_to_elem = np.zeros(q - 1, dtype=np.uint8)
    elem_to_power: dict[int, int] = {1: 0}
    value = 1
    for i in range(q - 1):
        power_to_elem[i] = value
        elem_to_power[int(value)] = i
        value = gf_multiply(value, primitive, m, prim_poly)
    return power_to_elem, elem_to_power



def evaluate_binary_polynomial(coeffs: Sequence[int], beta: int, m: int, prim_poly: int) -> int:
    value = 0
    power = 1
    for coeff in coeffs:
        if coeff:
            value ^= power
        power = gf_multiply(power, beta, m, prim_poly)
    return value



def minimal_polynomial(beta: int, m: int, prim_poly: int) -> np.ndarray:
    if beta == 0:
        return np.array([0, 1], dtype=np.uint8)
    for degree in range(1, m + 1):
        for mask in range(1 << degree):
            coeffs = np.array([(mask >> i) & 1 for i in range(degree)] + [1], dtype=np.uint8)
            if evaluate_binary_polynomial(coeffs, beta, m, prim_poly) == 0:
                return coeffs
    raise ValueError("No se encontró polinomio mínimo.")



def coeffs_to_poly_int(coeffs: Sequence[int]) -> int:
    poly = 0
    for i, coeff in enumerate(coeffs):
        if coeff:
            poly |= 1 << i
    return poly



def poly_int_to_coeffs(poly: int) -> np.ndarray:
    if poly == 0:
        return np.array([0], dtype=np.uint8)
    return np.array([(poly >> i) & 1 for i in range(gf_degree(poly) + 1)], dtype=np.uint8)



def poly_mul_gf2(a: int, b: int) -> int:
    result = 0
    aa = a
    bb = b
    while bb:
        if bb & 1:
            result ^= aa
        aa <<= 1
        bb >>= 1
    return result



def poly_divmod_gf2(a: int, b: int) -> tuple[int, int]:
    if b == 0:
        raise ZeroDivisionError("División polinomial por cero.")
    quotient = 0
    remainder = a
    deg_b = gf_degree(b)
    while remainder and gf_degree(remainder) >= deg_b:
        shift = gf_degree(remainder) - deg_b
        quotient ^= 1 << shift
        remainder ^= b << shift
    return quotient, remainder



def poly_gcd_gf2(a: int, b: int) -> int:
    x = a
    y = b
    while y:
        _, r = poly_divmod_gf2(x, y)
        x, y = y, r
    return x



def poly_lcm_gf2(a: int, b: int) -> int:
    if a == 0 or b == 0:
        return 0
    gcd = poly_gcd_gf2(a, b)
    quotient, remainder = poly_divmod_gf2(poly_mul_gf2(a, b), gcd)
    if remainder != 0:
        raise ValueError("El m.c.m. no es exacto.")
    return quotient



def binary_poly_to_string(poly: int | Sequence[int]) -> str:
    coeffs = poly_int_to_coeffs(poly) if isinstance(poly, int) else np.asarray(poly, dtype=np.uint8)
    terms = []
    for i in range(len(coeffs) - 1, -1, -1):
        if coeffs[i] == 0:
            continue
        if i == 0:
            terms.append("1")
        elif i == 1:
            terms.append("x")
        else:
            terms.append(f"x^{i}")
    return " + ".join(terms) if terms else "0"



def int_to_poly_string(value: int, m: int) -> str:
    if value == 0:
        return "0"
    terms = []
    for i in range(m - 1, -1, -1):
        if not (value >> i) & 1:
            continue
        if i == 0:
            terms.append("1")
        elif i == 1:
            terms.append("x")
        else:
            terms.append(f"x^{i}")
    return " + ".join(terms)



def field_element_to_string(value: int, elem_to_power: dict[int, int]) -> str:
    if value == 0:
        return "0"
    if value == 1:
        return "1"
    power = elem_to_power[value]
    return "α" if power == 1 else f"α^{power}"



def gf_addition_table(m: int) -> np.ndarray:
    q = 1 << m
    table = np.zeros((q, q), dtype=np.uint8)
    for i in range(q):
        for j in range(q):
            table[i, j] = i ^ j
    return table



def gf_multiplication_table(m: int, prim_poly: int) -> np.ndarray:
    q = 1 << m
    table = np.zeros((q, q), dtype=np.uint8)
    for i in range(q):
        for j in range(q):
            table[i, j] = gf_multiply(i, j, m, prim_poly)
    return table



def build_field(m: int, prim_poly: int) -> dict:
    primitive = find_primitive_element(m, prim_poly)
    power_to_elem, elem_to_power = build_log_tables(m, prim_poly, primitive)
    return {
        "m": m,
        "q": 1 << m,
        "prim_poly": prim_poly,
        "primitive": primitive,
        "power_to_elem": power_to_elem,
        "elem_to_power": elem_to_power,
        "add_table": gf_addition_table(m),
        "mul_table": gf_multiplication_table(m, prim_poly),
    }



def format_operation_table(table: np.ndarray, elem_to_power: dict[int, int]) -> str:
    q = table.shape[0]
    labels = [field_element_to_string(i, elem_to_power) for i in range(q)]
    widths = [max(len(label), 3) for label in labels]
    cell = max(max(widths), 3) + 1
    header = " ".join(label.rjust(cell) for label in ["*"] + labels)
    rows = [header]
    for i in range(q):
        row = [labels[i].rjust(cell)]
        for j in range(q):
            row.append(field_element_to_string(int(table[i, j]), elem_to_power).rjust(cell))
        rows.append(" ".join(row))
    return "\n".join(rows)


# ==============================
# Códigos de bloque
# ==============================


@dataclass
class HammingCode:
    m: int
    n: int
    k: int
    G: np.ndarray
    H: np.ndarray
    parity_positions: list[int]
    data_positions: list[int]
    syndrome_table: dict[tuple[int, ...], int]


@dataclass
class BCHCode:
    n: int
    k: int
    g_poly: int
    root_exponents: list[int]
    minimal_polynomials: dict[int, int]
    codebook: np.ndarray
    messages: np.ndarray



def linear_block_encode(message: np.ndarray, G: np.ndarray) -> np.ndarray:
    return (message @ G) % 2



def build_hamming74() -> HammingCode:
    G = np.array(
        [
            [1, 0, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 0, 1],
            [0, 0, 1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 1, 1],
        ],
        dtype=np.uint8,
    )
    H = np.array(
        [
            [1, 0, 1, 0, 1, 0, 1],
            [0, 1, 1, 0, 0, 1, 1],
            [0, 0, 0, 1, 1, 1, 1],
        ],
        dtype=np.uint8,
    )
    syndrome_table = {tuple(H[:, i].tolist()): i for i in range(H.shape[1])}
    return HammingCode(
        m=3,
        n=7,
        k=4,
        G=G,
        H=H,
        parity_positions=[5, 6, 7],
        data_positions=[1, 2, 3, 4],
        syndrome_table=syndrome_table,
    )



def build_general_hamming(m: int) -> HammingCode:
    n = (1 << m) - 1
    k = n - m
    H = np.array([[(col >> row) & 1 for col in range(1, n + 1)] for row in range(m)], dtype=np.uint8)
    parity_positions = [1 << i for i in range(m)]
    data_positions = [i for i in range(1, n + 1) if i not in parity_positions]

    def encode_block(message: np.ndarray) -> np.ndarray:
        codeword = np.zeros(n, dtype=np.uint8)
        codeword[np.array(data_positions) - 1] = message
        for parity_pos in parity_positions:
            involved = [idx - 1 for idx in range(1, n + 1) if (idx & parity_pos) and idx != parity_pos]
            parity_value = int(np.bitwise_xor.reduce(codeword[involved])) if involved else 0
            codeword[parity_pos - 1] = parity_value
        return codeword

    basis = np.eye(k, dtype=np.uint8)
    G = np.vstack([encode_block(basis_row) for basis_row in basis]).astype(np.uint8)
    syndrome_table = {tuple(H[:, i].tolist()): i for i in range(H.shape[1])}
    return HammingCode(
        m=m,
        n=n,
        k=k,
        G=G,
        H=H,
        parity_positions=parity_positions,
        data_positions=data_positions,
        syndrome_table=syndrome_table,
    )



def syndrome_decode_block(received: np.ndarray, code: HammingCode) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    syndrome = (received @ code.H.T) % 2
    corrected = received.copy()
    syndrome_key = tuple(int(x) for x in syndrome)
    if any(syndrome_key) and syndrome_key in code.syndrome_table:
        corrected[code.syndrome_table[syndrome_key]] ^= 1
    if code.data_positions == [1, 2, 3, 4] and code.n == 7:
        message = corrected[: code.k]
    else:
        message = corrected[np.array(code.data_positions) - 1]
    return message.astype(np.uint8), corrected.astype(np.uint8), syndrome.astype(np.uint8)



def bits_to_int_le(bits: Sequence[int]) -> int:
    value = 0
    for i, bit in enumerate(bits):
        value |= (int(bit) & 1) << i
    return value



def int_to_bits_le(value: int, length: int) -> np.ndarray:
    return np.array([(value >> i) & 1 for i in range(length)], dtype=np.uint8)



def cyclic_encode_systematic(message: np.ndarray, n: int, g_poly: int) -> np.ndarray:
    k = len(message)
    shift = n - k
    message_poly = bits_to_int_le(message)
    shifted = message_poly << shift
    _, remainder = poly_divmod_gf2(shifted, g_poly)
    codeword_poly = shifted ^ remainder
    return int_to_bits_le(codeword_poly, n)



def build_bch_15_7() -> BCHCode:
    m = 4
    n = 15
    prim_poly = 0b10011
    field = build_field(m, prim_poly)
    alpha = field["primitive"]
    minimal_polynomials: dict[int, int] = {}
    g_poly = 1
    for exp in [1, 2, 3, 4]:
        beta = gf_power(alpha, exp, m, prim_poly)
        min_poly = coeffs_to_poly_int(minimal_polynomial(beta, m, prim_poly))
        minimal_polynomials[exp] = min_poly
        g_poly = poly_lcm_gf2(g_poly, min_poly)
    degree = gf_degree(g_poly)
    k = n - degree
    messages = np.array([int_to_bits_le(i, k) for i in range(1 << k)], dtype=np.uint8)
    codebook = np.array([cyclic_encode_systematic(msg, n, g_poly) for msg in messages], dtype=np.uint8)
    return BCHCode(
        n=n,
        k=k,
        g_poly=g_poly,
        root_exponents=[1, 2, 3, 4],
        minimal_polynomials=minimal_polynomials,
        codebook=codebook,
        messages=messages,
    )



def decode_bch_ml_hard(received: np.ndarray, code: BCHCode) -> tuple[np.ndarray, np.ndarray]:
    distances = np.sum(code.codebook != received, axis=1)
    idx = int(np.argmin(distances))
    return code.messages[idx].copy(), code.codebook[idx].copy()



def decode_bch_ml_soft(received_symbols: np.ndarray, code: BCHCode) -> tuple[np.ndarray, np.ndarray]:
    expected = 1.0 - 2.0 * code.codebook.astype(float)
    metrics = np.sum((expected - received_symbols[None, :]) ** 2, axis=1)
    idx = int(np.argmin(metrics))
    return code.messages[idx].copy(), code.codebook[idx].copy()


# ==============================
# Modulación y canales
# ==============================



def bpsk_modulate(bits: np.ndarray) -> np.ndarray:
    return 1.0 - 2.0 * bits.astype(float)



def hard_demodulate(symbols: np.ndarray) -> np.ndarray:
    return (symbols < 0).astype(np.uint8)



def add_awgn(signal: np.ndarray, ebn0_db: float, rate: float, rng: np.random.Generator) -> np.ndarray:
    ebn0 = 10 ** (ebn0_db / 10.0)
    sigma = np.sqrt(1.0 / (2.0 * rate * ebn0))
    noise = sigma * rng.standard_normal(signal.shape)
    return signal + noise



def uncoded_bpsk_ber_theory(ebn0_db: np.ndarray) -> np.ndarray:
    ebn0 = 10 ** (ebn0_db / 10.0)
    return 0.5 * erfc(np.sqrt(ebn0))


# ==============================
# Códigos convolucionales y Viterbi
# ==============================



def octal_to_taps(octal_value: int, constraint_length: int) -> np.ndarray:
    taps = np.array(list(np.binary_repr(int(octal_value), width=constraint_length)), dtype=np.uint8)
    return taps



def state_to_bits(state: int, m: int) -> np.ndarray:
    return np.array([(state >> (m - 1 - i)) & 1 for i in range(m)], dtype=np.uint8)



def bits_to_state(bits: Sequence[int]) -> int:
    state = 0
    for bit in bits:
        state = (state << 1) | int(bit)
    return state



def build_trellis(generators_octal: Sequence[int], constraint_length: int) -> dict:
    generators = [octal_to_taps(g, constraint_length) for g in generators_octal]
    memory = constraint_length - 1
    n_outputs = len(generators)
    n_states = 1 << memory
    next_state = np.zeros((n_states, 2), dtype=np.int32)
    outputs = np.zeros((n_states, 2, n_outputs), dtype=np.uint8)
    outputs_bpsk = np.zeros((n_states, 2, n_outputs), dtype=float)

    for state in range(n_states):
        state_bits = state_to_bits(state, memory)
        for bit in (0, 1):
            register = np.concatenate(([bit], state_bits))
            out = np.array([int(np.sum(register * taps) % 2) for taps in generators], dtype=np.uint8)
            new_state_bits = register[:-1] if memory > 0 else np.array([], dtype=np.uint8)
            next_state[state, bit] = bits_to_state(new_state_bits)
            outputs[state, bit] = out
            outputs_bpsk[state, bit] = bpsk_modulate(out)

    return {
        "generators": generators,
        "constraint_length": constraint_length,
        "memory": memory,
        "n_states": n_states,
        "n_outputs": n_outputs,
        "next_state": next_state,
        "outputs": outputs,
        "outputs_bpsk": outputs_bpsk,
    }



def convolutional_encode(bits: np.ndarray, generators_octal: Sequence[int], constraint_length: int, terminate: bool = True) -> np.ndarray:
    trellis = build_trellis(generators_octal, constraint_length)
    memory = trellis["memory"]
    state_bits = np.zeros(memory, dtype=np.uint8)
    sequence = np.concatenate((bits, np.zeros(memory, dtype=np.uint8))) if terminate else bits.copy()
    encoded = []
    for bit in sequence:
        register = np.concatenate(([bit], state_bits))
        out = [int(np.sum(register * taps) % 2) for taps in trellis["generators"]]
        encoded.extend(out)
        if memory > 0:
            state_bits = register[:-1]
    return np.array(encoded, dtype=np.uint8)



def viterbi_decode_hard(received_bits: np.ndarray, generators_octal: Sequence[int], constraint_length: int, terminate: bool = True) -> np.ndarray:
    trellis = build_trellis(generators_octal, constraint_length)
    n_outputs = trellis["n_outputs"]
    rx = received_bits.reshape(-1, n_outputs)
    n_steps = rx.shape[0]
    n_states = trellis["n_states"]
    inf = 1e12

    path_metrics = np.full(n_states, inf, dtype=float)
    path_metrics[0] = 0.0
    survivors = np.full((n_steps, n_states), -1, dtype=np.int32)
    survivor_bits = np.zeros((n_steps, n_states), dtype=np.uint8)

    for t in range(n_steps):
        new_metrics = np.full(n_states, inf, dtype=float)
        for state in range(n_states):
            if path_metrics[state] >= inf:
                continue
            for bit in (0, 1):
                next_state = trellis["next_state"][state, bit]
                out = trellis["outputs"][state, bit]
                branch_metric = float(np.sum(out != rx[t]))
                candidate = path_metrics[state] + branch_metric
                if candidate < new_metrics[next_state]:
                    new_metrics[next_state] = candidate
                    survivors[t, next_state] = state
                    survivor_bits[t, next_state] = bit
        path_metrics = new_metrics

    state = 0 if terminate else int(np.argmin(path_metrics))
    decoded = np.zeros(n_steps, dtype=np.uint8)
    for t in range(n_steps - 1, -1, -1):
        decoded[t] = survivor_bits[t, state]
        state = survivors[t, state]
        if state < 0:
            state = 0
    if terminate and trellis["memory"] > 0:
        decoded = decoded[:-trellis["memory"]]
    return decoded.astype(np.uint8)



def viterbi_decode_soft(received_symbols: np.ndarray, generators_octal: Sequence[int], constraint_length: int, terminate: bool = True) -> np.ndarray:
    trellis = build_trellis(generators_octal, constraint_length)
    n_outputs = trellis["n_outputs"]
    rx = received_symbols.reshape(-1, n_outputs)
    n_steps = rx.shape[0]
    n_states = trellis["n_states"]
    inf = 1e12

    path_metrics = np.full(n_states, inf, dtype=float)
    path_metrics[0] = 0.0
    survivors = np.full((n_steps, n_states), -1, dtype=np.int32)
    survivor_bits = np.zeros((n_steps, n_states), dtype=np.uint8)

    for t in range(n_steps):
        new_metrics = np.full(n_states, inf, dtype=float)
        for state in range(n_states):
            if path_metrics[state] >= inf:
                continue
            for bit in (0, 1):
                next_state = trellis["next_state"][state, bit]
                out = trellis["outputs_bpsk"][state, bit]
                branch_metric = float(np.sum((rx[t] - out) ** 2))
                candidate = path_metrics[state] + branch_metric
                if candidate < new_metrics[next_state]:
                    new_metrics[next_state] = candidate
                    survivors[t, next_state] = state
                    survivor_bits[t, next_state] = bit
        path_metrics = new_metrics

    state = 0 if terminate else int(np.argmin(path_metrics))
    decoded = np.zeros(n_steps, dtype=np.uint8)
    for t in range(n_steps - 1, -1, -1):
        decoded[t] = survivor_bits[t, state]
        state = survivors[t, state]
        if state < 0:
            state = 0
    if terminate and trellis["memory"] > 0:
        decoded = decoded[:-trellis["memory"]]
    return decoded.astype(np.uint8)


# ==============================
# Simulaciones BER
# ==============================



def simulate_bsc_block_code(
    encode_fn: Callable[[np.ndarray], np.ndarray],
    decode_fn: Callable[[np.ndarray], np.ndarray],
    k: int,
    p_values: np.ndarray,
    total_info_bits: int,
    rng: np.random.Generator,
) -> np.ndarray:
    n_blocks = int(np.ceil(total_info_bits / k))
    ber = []
    for p in p_values:
        info = rng.integers(0, 2, size=(n_blocks, k), dtype=np.uint8)
        coded = np.array([encode_fn(block) for block in info], dtype=np.uint8)
        flips = (rng.random(coded.shape) < p).astype(np.uint8)
        received = coded ^ flips
        decoded = np.array([decode_fn(block) for block in received], dtype=np.uint8)
        errors = np.sum(decoded[:, :k] != info)
        ber.append(errors / (n_blocks * k))
    return np.array(ber, dtype=float)



def simulate_awgn_hamming(
    code: HammingCode,
    ebn0_db_values: np.ndarray,
    total_info_bits: int,
    rng: np.random.Generator,
) -> np.ndarray:
    n_blocks = int(np.ceil(total_info_bits / code.k))
    ber = []
    for ebn0_db in ebn0_db_values:
        info = rng.integers(0, 2, size=(n_blocks, code.k), dtype=np.uint8)
        coded = np.array([linear_block_encode(block, code.G) for block in info], dtype=np.uint8)
        tx = bpsk_modulate(coded.reshape(-1))
        rx = add_awgn(tx, float(ebn0_db), rate=code.k / code.n, rng=rng)
        hard = hard_demodulate(rx).reshape(n_blocks, code.n)
        decoded = np.array([syndrome_decode_block(block, code)[0] for block in hard], dtype=np.uint8)
        ber.append(np.mean(decoded[:, : code.k] != info))
    return np.array(ber, dtype=float)



def simulate_convolutional_awgn(
    generators_octal: Sequence[int],
    constraint_length: int,
    ebn0_db_values: np.ndarray,
    total_info_bits: int,
    rng: np.random.Generator,
    decision: str = "soft",
) -> np.ndarray:
    info = rng.integers(0, 2, size=total_info_bits, dtype=np.uint8)
    coded = convolutional_encode(info, generators_octal, constraint_length, terminate=True)
    rate = total_info_bits / len(coded)
    tx = bpsk_modulate(coded)
    ber = []
    for ebn0_db in ebn0_db_values:
        rx = add_awgn(tx, float(ebn0_db), rate=rate, rng=rng)
        if decision == "hard":
            decoded = viterbi_decode_hard(hard_demodulate(rx), generators_octal, constraint_length, terminate=True)
        else:
            decoded = viterbi_decode_soft(rx, generators_octal, constraint_length, terminate=True)
        ber.append(np.mean(decoded[:total_info_bits] != info))
    return np.array(ber, dtype=float)


# ==============================
# Espacio de señal
# ==============================



def inner_product(x: np.ndarray, y: np.ndarray, t: np.ndarray) -> float:
    return float(np.trapezoid(x * y, t))



def gram_schmidt(functions: list[np.ndarray], t: np.ndarray) -> list[np.ndarray]:
    basis = []
    for g in functions:
        v = g.astype(float).copy()
        for phi in basis:
            v -= inner_product(v, phi, t) * phi
        norm = np.sqrt(inner_product(v, v, t))
        if norm < 1e-12:
            raise ValueError("Las funciones no son linealmente independientes.")
        basis.append(v / norm)
    return basis



def project_pca_2d(X: np.ndarray) -> np.ndarray:
    Xc = X - np.mean(X, axis=0, keepdims=True)
    _, _, vt = np.linalg.svd(Xc, full_matrices=False)
    return Xc @ vt[:2].T


# ==============================
# Figuras
# ==============================



def plot_gram_schmidt(fig_dir: Path) -> None:
    t = np.linspace(0.0, 1.0, 1000)
    g1 = np.ones_like(t)
    g2 = t
    phi1, phi2 = gram_schmidt([g1, g2], t)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.5))
    axes[0].plot(t, g1, label=r"$g_1(t)=1$", lw=2)
    axes[0].plot(t, g2, label=r"$g_2(t)=t$", lw=2)
    axes[0].set_title("Señales originales")
    axes[0].set_xlabel("t")
    axes[0].grid(True, alpha=0.3)
    axes[0].legend()

    axes[1].plot(t, phi1, label=r"$\phi_1(t)$", lw=2)
    axes[1].plot(t, phi2, label=r"$\phi_2(t)$", lw=2)
    axes[1].set_title("Base ortonormal por Gram-Schmidt")
    axes[1].set_xlabel("t")
    axes[1].grid(True, alpha=0.3)
    axes[1].legend()

    fig.tight_layout()
    fig.savefig(fig_dir / "unidad4_gram_schmidt.png", dpi=180, bbox_inches="tight")
    plt.close(fig)



def plot_minimum_distance(fig_dir: Path, code: HammingCode) -> None:
    messages = np.array([int_to_bits_le(i, code.k) for i in range(1 << code.k)], dtype=np.uint8)
    codewords = np.array([linear_block_encode(msg, code.G) for msg in messages], dtype=np.uint8)
    bipolar = bpsk_modulate(codewords)
    projected = project_pca_2d(bipolar)

    distances = np.linalg.norm(bipolar[:, None, :] - bipolar[None, :, :], axis=2)
    distances += np.eye(len(distances)) * 1e9
    i_min, j_min = np.unravel_index(np.argmin(distances), distances.shape)
    dmin_hamming = int(np.min(np.sum(codewords[:, None, :] != codewords[None, :, :], axis=2) + np.eye(len(codewords), dtype=int) * 99))
    dmin_euclid = float(distances[i_min, j_min])

    fig, ax = plt.subplots(figsize=(7, 6))
    ax.scatter(projected[:, 0], projected[:, 1], s=55, alpha=0.75, label="Palabras-código BPSK")
    ax.plot(
        [projected[i_min, 0], projected[j_min, 0]],
        [projected[i_min, 1], projected[j_min, 1]],
        "r--",
        lw=2,
        label=f"Par más cercano, d≈{dmin_euclid:.2f}",
    )
    ax.scatter(projected[[i_min, j_min], 0], projected[[i_min, j_min], 1], c="red", s=90)
    ax.set_title(f"Visualización de distancia mínima del Hamming (7,4)\n$d_H^{{min}}={dmin_hamming}$, $d_E^{{min}}=2\\sqrt{{3}}\approx{dmin_euclid:.2f}$")
    ax.set_xlabel("Componente principal 1")
    ax.set_ylabel("Componente principal 2")
    ax.grid(True, alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(fig_dir / "unidad4_distancia_minima.png", dpi=180, bbox_inches="tight")
    plt.close(fig)



def plot_block_bsc_curves(fig_dir: Path, rng: np.random.Generator, mode: str) -> dict:
    p_values = np.logspace(-3.0, -1.0, 7)
    total_bits = 12000 if mode == "rapido" else 40000

    h74 = build_hamming74()
    h15 = build_general_hamming(4)
    bch = build_bch_15_7()

    ber_h74 = simulate_bsc_block_code(
        encode_fn=lambda u: linear_block_encode(u, h74.G),
        decode_fn=lambda r: syndrome_decode_block(r, h74)[0],
        k=h74.k,
        p_values=p_values,
        total_info_bits=total_bits,
        rng=rng,
    )
    ber_h15 = simulate_bsc_block_code(
        encode_fn=lambda u: linear_block_encode(u, h15.G),
        decode_fn=lambda r: syndrome_decode_block(r, h15)[0],
        k=h15.k,
        p_values=p_values,
        total_info_bits=total_bits,
        rng=rng,
    )
    ber_bch = simulate_bsc_block_code(
        encode_fn=lambda u: cyclic_encode_systematic(u, bch.n, bch.g_poly),
        decode_fn=lambda r: decode_bch_ml_hard(r, bch)[0],
        k=bch.k,
        p_values=p_values,
        total_info_bits=total_bits,
        rng=rng,
    )

    fig, ax = plt.subplots(figsize=(8, 5.5))
    ax.semilogy(p_values, ber_h74, "o-", lw=2, label="Hamming (7,4)")
    ax.semilogy(p_values, ber_h15, "s-", lw=2, label="Hamming (15,11)")
    ax.semilogy(p_values, ber_bch, "^-", lw=2, label="BCH (15,7) simplificado")
    ax.set_title("BER en canal BSC para códigos de bloque")
    ax.set_xlabel("Probabilidad de cruce p")
    ax.set_ylabel("BER")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(fig_dir / "unidad4_ber_bsc_bloques.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    return {
        "p_values": p_values,
        "ber_h74": ber_h74,
        "ber_h15": ber_h15,
        "ber_bch": ber_bch,
        "bch": bch,
        "h15": h15,
    }



def plot_awgn_comparison(fig_dir: Path, rng: np.random.Generator, mode: str) -> dict:
    ebn0_db = np.arange(0, 6 if mode == "rapido" else 7, 1, dtype=float)
    bits_hamming = 16000 if mode == "rapido" else 50000
    bits_conv_small = 2500 if mode == "rapido" else 9000
    bits_conv_large = 1800 if mode == "rapido" else 6000

    h74 = build_hamming74()
    ber_uncoded = uncoded_bpsk_ber_theory(ebn0_db)
    ber_hamming = simulate_awgn_hamming(h74, ebn0_db, bits_hamming, rng)
    ber_conv_k3_hard = simulate_convolutional_awgn([0o7, 0o5], 3, ebn0_db, bits_conv_small, rng, decision="hard")
    ber_conv_k3_soft = simulate_convolutional_awgn([0o7, 0o5], 3, ebn0_db, bits_conv_small, rng, decision="soft")
    ber_conv_k7_soft = simulate_convolutional_awgn([0o171, 0o133], 7, ebn0_db, bits_conv_large, rng, decision="soft")

    fig, ax = plt.subplots(figsize=(8.5, 5.8))
    ax.semilogy(ebn0_db, ber_uncoded, "k--", lw=2, label="BPSK sin codificación (teórico)")
    ax.semilogy(ebn0_db, ber_hamming, "o-", lw=2, label="Hamming (7,4) + decisión dura")
    ax.semilogy(ebn0_db, ber_conv_k3_hard, "s-", lw=2, label="Conv. [7,5], K=3, Viterbi duro")
    ax.semilogy(ebn0_db, ber_conv_k3_soft, "d-", lw=2, label="Conv. [7,5], K=3, Viterbi suave")
    ax.semilogy(ebn0_db, ber_conv_k7_soft, "^-", lw=2, label="Conv. [171,133], K=7, Viterbi suave")
    ax.set_title("BER vs $E_b/N_0$: sin codificar, Hamming y convolucional")
    ax.set_xlabel(r"$E_b/N_0$ (dB)")
    ax.set_ylabel("BER")
    ax.set_ylim(1e-5, 3e-1)
    ax.grid(True, which="both", alpha=0.3)
    ax.legend(fontsize=9)
    fig.tight_layout()
    fig.savefig(fig_dir / "unidad4_ber_awgn_comparacion.png", dpi=180, bbox_inches="tight")
    plt.close(fig)

    return {
        "ebn0_db": ebn0_db,
        "ber_uncoded": ber_uncoded,
        "ber_hamming": ber_hamming,
        "ber_conv_k3_hard": ber_conv_k3_hard,
        "ber_conv_k3_soft": ber_conv_k3_soft,
        "ber_conv_k7_soft": ber_conv_k7_soft,
    }



def plot_hard_vs_soft(fig_dir: Path, curves: dict) -> None:
    fig, ax = plt.subplots(figsize=(7.8, 5.2))
    ax.semilogy(curves["ebn0_db"], curves["ber_conv_k3_hard"], "o-", lw=2, label="Viterbi duro")
    ax.semilogy(curves["ebn0_db"], curves["ber_conv_k3_soft"], "s-", lw=2, label="Viterbi suave")
    ax.set_title("Cadena codificada completa: decisión dura vs. suave")
    ax.set_xlabel(r"$E_b/N_0$ (dB)")
    ax.set_ylabel("BER")
    ax.grid(True, which="both", alpha=0.3)
    ax.legend()
    fig.tight_layout()
    fig.savefig(fig_dir / "unidad4_dura_vs_suave.png", dpi=180, bbox_inches="tight")
    plt.close(fig)



def required_ebn0_at_target(ebn0_db: np.ndarray, ber: np.ndarray, target_ber: float) -> float | None:
    valid = np.logical_and(ber > 0, np.isfinite(ber))
    if np.count_nonzero(valid) < 2:
        return None
    x = np.log10(ber[valid])
    y = ebn0_db[valid]
    order = np.argsort(x)
    x_sorted = x[order]
    y_sorted = y[order]
    x_target = np.log10(target_ber)
    if not (x_sorted[0] <= x_target <= x_sorted[-1]):
        return None
    interpolator = interp1d(x_sorted, y_sorted, kind="linear")
    return float(interpolator(x_target))



def plot_coding_gain(fig_dir: Path, curves: dict, target_ber: float = 1e-3) -> float | None:
    eb_uncoded = required_ebn0_at_target(curves["ebn0_db"], curves["ber_uncoded"], target_ber)
    eb_coded = required_ebn0_at_target(curves["ebn0_db"], curves["ber_conv_k7_soft"], target_ber)
    if eb_uncoded is None or eb_coded is None:
        return None
    gain = eb_uncoded - eb_coded

    fig, ax = plt.subplots(figsize=(6.5, 4.8))
    ax.bar(["Sin codificar", "Conv. K=7"], [eb_uncoded, eb_coded], color=["tab:gray", "tab:blue"])
    ax.set_ylabel(r"$E_b/N_0$ requerido (dB)")
    ax.set_title(f"Ganancia de codificación a BER={target_ber:.0e}\nGanancia ≈ {gain:.2f} dB")
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    fig.savefig(fig_dir / "unidad4_ganancia_codificacion.png", dpi=180, bbox_inches="tight")
    plt.close(fig)
    return gain


# ==============================
# Resúmenes impresos
# ==============================



def print_gf_summary(print_tables: bool = False) -> None:
    gf23 = build_field(3, 0b1011)
    gf24 = build_field(4, 0b10011)

    print("\n=== Aritmética en campos de Galois ===")
    print("GF(2) - tabla de suma:")
    print(gf2_add_table())
    print("GF(2) - tabla de multiplicación:")
    print(gf2_mul_table())

    for field in [gf23, gf24]:
        m = field["m"]
        prim_poly = field["prim_poly"]
        primitive = field["primitive"]
        elem_to_power = field["elem_to_power"]
        alpha = primitive
        min_alpha = coeffs_to_poly_int(minimal_polynomial(alpha, m, prim_poly))
        min_alpha3 = coeffs_to_poly_int(minimal_polynomial(gf_power(alpha, 3, m, prim_poly), m, prim_poly))
        print(f"\nGF(2^{m}) con polinomio irreducible p(x)={binary_poly_to_string(prim_poly)}")
        print(f"Elemento primitivo encontrado: {field_element_to_string(primitive, elem_to_power)} = {int_to_poly_string(primitive, m)}")
        print(f"Orden multiplicativo: {gf_order(primitive, m, prim_poly)}")
        print(f"Polinomio mínimo de α: {binary_poly_to_string(min_alpha)}")
        print(f"Polinomio mínimo de α^3: {binary_poly_to_string(min_alpha3)}")
        if print_tables:
            print("\nTabla de suma:")
            print(format_operation_table(field["add_table"], elem_to_power))
            print("\nTabla de multiplicación:")
            print(format_operation_table(field["mul_table"], elem_to_power))



def print_code_summary(block_results: dict) -> None:
    h74 = build_hamming74()
    h15 = block_results["h15"]
    bch = block_results["bch"]

    print("\n=== Códigos de bloque ===")
    print("Matriz generadora Hamming (7,4):")
    print(h74.G)
    print("Matriz de chequeo Hamming (7,4):")
    print(h74.H)
    print(f"Hamming (15,11): n={h15.n}, k={h15.k}, paridades={h15.parity_positions}")
    print("BCH (15,7) simplificado desde raíces consecutivas α, α^2, α^3, α^4:")
    for exp, min_poly in sorted(bch.minimal_polynomials.items()):
        print(f"  M_α^{exp}(x) = {binary_poly_to_string(min_poly)}")
    print(f"  g(x) = {binary_poly_to_string(bch.g_poly)}")


# ==============================
# Programa principal
# ==============================



def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simulación de la Unidad 4: Codificación de canal.")
    parser.add_argument("--modo", choices=["rapido", "completo"], default="rapido", help="Carga de simulación.")
    parser.add_argument("--semilla", type=int, default=1234, help="Semilla pseudoaleatoria.")
    parser.add_argument("--tablas-gf", action="store_true", help="Imprime tablas completas de GF(2^3) y GF(2^4).")
    parser.add_argument("--sin-figuras", action="store_true", help="Ejecuta cálculos pero no guarda figuras.")
    return parser.parse_args()



def main() -> None:
    args = parse_args()
    rng = np.random.default_rng(args.semilla)
    fig_dir = asegurar_directorio(Path(__file__).resolve().parent.parent / "figuras")

    print_gf_summary(print_tables=args.tablas_gf)

    if not args.sin_figuras:
        plot_gram_schmidt(fig_dir)
        plot_minimum_distance(fig_dir, build_hamming74())

    block_results = plot_block_bsc_curves(fig_dir, rng, args.modo) if not args.sin_figuras else {
        "h15": build_general_hamming(4),
        "bch": build_bch_15_7(),
    }
    print_code_summary(block_results)

    if not args.sin_figuras:
        awgn_results = plot_awgn_comparison(fig_dir, rng, args.modo)
        plot_hard_vs_soft(fig_dir, awgn_results)
        gain = plot_coding_gain(fig_dir, awgn_results, target_ber=1e-3)
        if gain is not None:
            print(f"\nGanancia de codificación aproximada a BER=1e-3: {gain:.2f} dB")
        else:
            print("\nNo fue posible interpolar la ganancia de codificación en el rango simulado.")
        print(f"Figuras guardadas en: {fig_dir}")


if __name__ == "__main__":
    main()
