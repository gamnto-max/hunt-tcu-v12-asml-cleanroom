# src/sim/Q0005_app.py
# Project: HUNT-QSoC "Continuum" v1.2 (ASML Cleanroom Suite)
# Symmetry: Interactive App for Dynamic Thermal Stress Optimization (Q0005 Tier)

import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. ENTORNO CRÍTICO DE ALTA VELOCIDAD PARA STREAMLIT CLOUD
st.set_page_config(
    page_title="HUNT-QSoC v1.2 - Eslabón Q0005",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estética de laboratorio: Centrado geométrico absoluto y estilo neón para portátiles
st.markdown("""
    <style>
        .stAppDeployButton { display: none; }
        
        /* Contenedor central simétrico */
        .block-container {
            max-width: 1000px !important;
            margin: 0 auto !important;
            float: none !important;
            border-top: 10px solid #00ffaa;
            box-shadow: 0 -15px 30px rgba(0, 255, 170, 0.4);
            padding-top: 2rem;
            padding-bottom: 2rem;
            background-color: #020305 !important;
        }
        
        h1, h2, h3, p, .stMarkdown {
            text-align: center !important;
        }
        
        /* Caja de Consola Térmica Industrial */
        .console-box {
            background-color: #090d16 !important;
            border: 1px solid #1f3a60 !important;
            border-left: 4px solid #00ffaa !important;
            padding: 15px !important;
            border-radius: 5px !important;
            font-family: 'Courier New', monospace !important;
            color: #e0e6ed !important;
            margin: 15px auto !important;
            max-width: 800px !important;
            text-align: left !important;
        }
        
        .console-title {
            color: #00ffaa !important;
            font-weight: bold !important;
            margin-bottom: 5px !important;
        }
        
        [data-testid="stMetricValue"] {
            color: #00ffaa !important;
            font-family: 'Courier New', monospace;
            text-align: center !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🌡️ PROTOCOLO DE CALIBRACIÓN DE ESTRÉS TÉRMICO — ESLABÓN Q0005")
st.markdown("<p style='color:#8a9a9a; font-size:16px;'><b>SÚPER-CHIP CUÁNTICO CONTINUUM v1.2</b><br>Compensación Dinámica por Dilatación Molecular en el Cristal de Silicio-28</p>", unsafe_allow_html=True)

# =========================================================================
# CONTROLADORES DE TEMPERATURA EN LA BARRA LATERAL
# =========================================================================
st.sidebar.header("🎛️ Simulación de Sala Blanca")
thermal_lock = st.sidebar.checkbox("Activar Células Peltier", value=True)
cleanroom_temp = st.sidebar.slider("Temperatura Inducida (°C)", 23.00, 25.00, 24.15, step=0.01)

if "q_frame_5" not in st.session_state:
    st.session_state.q_frame_5 = 0.0

# Cálculo matemático del desfase angular real provocado por el calor
delta_t = cleanroom_temp - 24.00
phase_drift_rad = delta_t * np.pi * 0.25

if thermal_lock and abs(delta_t) < 0.85:
    st.session_state.q_frame_5 += 0.12
    stabilizer_status = "ESTABILIZADOR ACTIVO - COMPENSANDO FASE"
    color_status = "#00ffaa"
    residual_error = 0.0000000000000000
else:
    stabilizer_status = "CRÍTICO - DESACOPLAMIENTO POR TEMPERATURA"
    color_status = "#ff4b4b"
    residual_error = abs(delta_t) * 0.15

# =========================================================================
# CONSOLA INDUSTRIAL INTEGRADA Y CENTRADA
# =========================================================================
st.markdown("### 🖥️ Reporte del Monitor de Compensación Pasiva (Q0005_core.v)")
st.markdown(f"""
<div class="console-box" style="border-left: 4px solid {color_status} !important;">
    <div class="console-title" style="color: {color_status} !important;">>>> MONITOR DE DILATACIÓN MOLECULAR DEL SILICIO-28</div>
    • Punto de Control: Objetivo Térmico Fijo @ 24.00 °C | Lectura Actual: {cleanroom_temp:.2f} °C<br>
    • Desfase Angular : {phase_drift_rad:.4f} Radianes inducidos en la red cristalina<br>
    • Estado del SoC  : {stabilizer_status}<br>
    • Bus de 64 bits   : Formato Q32.32 Coherente con QRAM de 128 GB Compartida<br>
    • Error de Salida  : Residuo Vectorial = {residual_error:.16f} | Latencia: 0.00 ns
</div>
""", unsafe_allow_html=True)

# =========================================================================
# OSCILOSCOPIO CINÉTICO TÉRMICO CENTRADO
# =========================================================================
st.markdown("### 🌊 Comportamiento del Bus Cuántico bajo Estrés")

x_space = np.linspace(0, 4 * np.pi, 250)
if thermal_lock:
    # Simulación de la onda portadora deformada por calor y la compensación del antinodo
    y_signal = 1.250 * np.sin(x_space)
    y_thermal_noise = 0.80 * np.sin(phase_drift_rad) * np.cos(x_space + st.session_state.q_frame_5)
    y_anti_thermal = -1.0 * y_thermal_noise
    y_qram_out = y_signal + y_thermal_noise + y_anti_thermal # Teorema de Hunt absoluto
else:
    y_signal = np.zeros(250)
    y_thermal_noise = np.zeros(250)
    y_anti_thermal = np.zeros(250)
    y_qram_out = np.zeros(250)

df_thermal_matrix = pd.DataFrame({
    'Coordenada Red Cristalina': x_space,
    'Señal Útil de Videojuegos': y_signal,
    'Ruido por Dilatación Térmica': y_thermal_noise,
    'Antinodo Hunt Adaptativo': y_anti_thermal,
    'Bus de Salida Estable (QRAM)': y_qram_out
})

st.line_chart(df_thermal_matrix, x='Coordenada Red Cristalina', height=350)

# =========================================================================
# MÉTRICAS CUANTITATIVAS EN TIEMPO REAL
# =========================================================================
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Margen de Tolerancia Térmica", value="± 0.85 °C", delta="Control Peltier OK")
with col2:
    st.metric(label="Error en el Bus Coherente", value=f"{residual_error:.6f}", delta="Cero Absoluto")
with col3:
    st.metric(label="Retardo Acoplamiento QRAM", value="0.00 ns", delta="Invariante Rígida")

# Lazo de refresco continuo para mantener el show fluido en la nube de Streamlit
if thermal_lock and abs(delta_t) < 0.85:
    time.sleep(0.03)
    st.rerun()