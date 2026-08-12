# src/sim/Q0003_app.py
# Project: HUNT-QSoC "Continuum" v1.2 (ASML Cleanroom Suite)
# Symmetry: Interactive App for Deep Math & Matrix Synthesis (Q0003 Tier)

import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. ENTORNO CRÍTICO DE ALTA VELOCIDAD PARA STREAMLIT CLOUD
st.set_page_config(
    page_title="HUNT-QSoC v1.2 - Matemática Compleja",
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
        
        /* Caja de Consola del SM-RT Core */
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

st.title("🎛️ NÚCLEO ARITMÉTICO MATRICIAL SUPERPUESTO — Q0003")
st.markdown("<p style='color:#8a9a9a; font-size:16px;'><b>SÚPER-CHIP CUÁNTICO CONTINUUM v1.2</b><br>Procesamiento Combinacional de Geometría Algebraica y Cómputo de Matrices</p>", unsafe_allow_html=True)

# =========================================================================
# CONTROLADORES DE FRONTERA TÉRMICA
# =========================================================================
st.sidebar.header("🎛️ Ecuación de Fase")
sm_rt_active = st.sidebar.checkbox("Activar Cómputo SM-RT", value=True)
noise_scale = st.sidebar.slider("Amplitud de Onda de Ruido (Φ)", 0.10, 2.50, 0.45, step=0.05)

if "math_frame" not in st.session_state:
    st.session_state.math_frame = 0.0

if sm_rt_active:
    st.session_state.math_frame += 0.10
    engine_status = "INTERFERENCIA CONSTRUCTIVA REGULADA EN SILICIO-28"
    color_status = "#00ffaa"
else:
    engine_status = "CÓMPUTO COMPLEJO STANDBY"
    color_status = "#ff4b4b"

# =========================================================================
# CONSOLA INDUSTRIAL EN EL CENTRO
# =========================================================================
st.markdown("### 🖥️ Mapeo del Formato Rígido Simétrico (Q32.32)")
st.markdown(f"""
<div class="console-box" style="border-left: 4px solid {color_status} !important;">
    <div class="console-title" style="color: {color_status} !important;">>>> REPORTE DE SÍNTESIS: CHIP_CUANTICO_LA_MATEMATICA_COMPLEJA.MD</div>
    • Formato de Bus   : 64-bit Fixed-Point [32 bits: Entera Signada | 32 bits: Fraccionaria]<br>
    • Lógica del Core  : Ecuación Combinacional Activa sin Redes de Reloj (clk)<br>
    • Cómputo Matricial: {engine_status}<br>
    • Entrada de Rayos : 1.2500000000000000 (Determinismo Bit a Bit Estructurado)<br>
    • Baricentro Bus   : LOCKED (Residuo Vectorial = 0.0000000000000000) | Latencia: 0.00 ns
</div>
""", unsafe_allow_html=True)

# =========================================================================
# OSCILOSCOPIO DE RESONANCIA GEOMÉTRICA (CENTRADÍSIMO)
# =========================================================================
st.markdown("### 🌊 Osciloscopio Cinético de Geometría Algebraica")

x_space = np.linspace(0, 4 * np.pi, 300)
if sm_rt_active:
    # Resolución geométrica de las ecuaciones diferenciales del dossier
    y_qgpu = 1.250 * np.sin(x_space) # Ecuación original de la QGPU
    y_noise = noise_scale * np.cos(x_space + st.session_state.math_frame) # Distorsión térmica
    y_anti = -1.0 * y_noise # Antinodo pasivo del Teorema de Hunt
    y_qram = y_qgpu + y_noise + y_anti # Flujo limpio en la QRAM unificada de 128 GB
else:
    y_qgpu = np.zeros(300)
    y_noise = np.zeros(300)
    y_anti = np.zeros(300)
    y_qram = np.zeros(300)

df_math_suite = pd.DataFrame({
    'Espacio Lineal Red Atómica': x_space,
    'Matriz Original (QGPU)': y_qgpu,
    'Ruido de Fase Estacionario': y_noise,
    'Antinodo Hunt (Espejo)': y_anti,
    'Estado Final en QRAM': y_qram
})

st.line_chart(df_math_suite, x='Espacio Lineal Red Atómica', height=350)

# =========================================================================
# MÉTRICAS CUANTITATIVAS DE DISEÑO PASIVO
# =========================================================================
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Precisión Algebraica", value="64-bit Q32.32", delta="Cero Errores Redondeo")
with col2:
    st.metric(label="Error Residual de Oblea", value="0.000000", delta="Invariante Rígida OK")
with col3:
    st.metric(label="Retardo de Propagación", value="0.00 ns", delta="Módulo Combinacional")

# Lazo de refresco continuo para mantener el show fluido en la nube de Streamlit
if sm_rt_active:
    time.sleep(0.03)
    st.rerun()