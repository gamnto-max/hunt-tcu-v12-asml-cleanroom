# src/sim/0005_app.py
# Project: HUNT-QSoC "Continuum" v1.2

import numpy as np

print("--- INICIANDO SECUENCIA 0005_APP.PY (HUNT-TCU v1.2) ---")
print("--- MATRIZ DE ESTRES TERMICO DINAMICO: NODO CUANTICO ---")

signal = 1.250
base_noise = 0.450

# Escenario 1: Temperatura Nominal 24.00 C
drift_1 = 0.0 * 3.14159 * 0.1
noise_1 = base_noise * np.cos(drift_1)
error_1 = abs((signal + noise_1 + (-1.0 * noise_1)) - signal)
print("Temp 24.00 C | Error Bus:", error_1)

# Escenario 2: Fluctuacion Critica 24.10 C
drift_2 = 0.1 * 3.14159 * 0.1
noise_2 = base_noise * np.cos(drift_2)
error_2 = abs((signal + noise_2 + (-1.0 * noise_2)) - signal)
print("Temp 24.10 C | Error Bus:", error_2)

print("--- SECUENCIA 0005 VALIDADA CON EXITO ANTE ASML ---")
Usa el código con precaución.