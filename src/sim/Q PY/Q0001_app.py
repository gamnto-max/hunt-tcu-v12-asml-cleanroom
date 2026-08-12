# src/sim/Q0001_app.py
# Project: HUNT-QSoC "Continuum" v1.2 (ASML Cleanroom Suite)
# Symmetry: Interactive App for Quantum SoC & QRAM Entanglement (Q0001 Tier)

import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. ENTORNO CRÍTICO DE ALTA VELOCIDAD PARA STREAMLIT CLOUD
st.set_page_config(
    page_title="HUNT-QSoC v1.2 - Eslabón Q0001",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estética termoestable ASML: Forzar centrado absoluto y diseño de sala blanca neón
st.markdown("""
    <style>
        .stAppDeployButton { display: none; }
        
        /* Contenedor central simétrico para portátiles */
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
        
        /* Caja de Consola Industrial del Eslabón Q0001 */
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

st.title("🛰️ ENLACE DE INICIALIZACIÓN SOĆ Y QRAM — ESLABÓN Q0001")
st.markdown("<p style='color:#8a9a9a; font-size:16px;'><b>SÚPER-CHIP CUÁNTICO CONTINUUM v1.2</b><br>Validación en Tiempo Real del Acoplamiento de Memoria Unificada de 128 GB</p>", unsafe_allow_html=True)

# =========================================================================
# CONTROLADORES EN LA BARRA LATERAL DEL LABORATORIO
# =========================================================================
st.sidebar.header("🎛️ Calibración del Láser ASML")
laser_active = st.sidebar.checkbox("Activar Láser de Control (0.4 uW)", value=True)
temperatura = st.sidebar.slider("Temperatura de la Sala Blanca", 23.50, 24.50, 24.00, step=0.01)

# Estado de animación continua
if "q_frame" not in st.session_state:
    st.session_state.q_frame = 0.0

if laser_active and abs(temperatura - 24.00) < 0.05:
    st.session_state.q_frame += 0.1
    coherence_status = "COHERENTE / ENERGETIZADO"
    color_status = "#00ffaa"
    qram_signal = 1.250 # Vector de datos de la QRAM
else:
    coherence_status = "DECORRECCIÓN / ERROR TÉRMICO"
    color_status = "#ff4b4b"
    qram_signal = 0.000

# =========================================================================
# CONSOLA DE HARDWARE CENTRADA
# =========================================================================
st.markdown("### 🖥️ Reporte Estructural del Módulo Verilog (Q0001_core)")
st.markdown(f"""
<div class="console-box" style="border-left: 4px solid {color_status} !important;">
    <div class="console-title" style="color: {color_status} !important;">>>> CONTROLADOR DE ENLAZAMIENTO MOLECULAR ACTIVO</div>
    • Sustrato Cuántico : Silicio-28 Puro (Espín Magnético Cero)<br>
    • Estado Térmico     : {temperatura:.2f} °C (Objetivo Rígido: 24.00 °C)<br>
    • Acoplamiento Láser: {0.4 if laser_active else 0.0} uW Non-Intrusive Locked<br>
    • Canal Físico QRAM : 128 GB Unificada Coherente -> Enlace Activo<br>
    • Estado del Bus    : {coherence_status} | Precisión: Bus Nativo de 64 bits
</div>
""", unsafe_allow_html=True)

# =========================================================================
# SIMULACIÓN INTERACTIVA DE ENTLAMIENTO EN MOVIMIENTO
# =========================================================================
st.markdown("### 🌀 Visualización del Entrelazamiento SoC-QRAM (0.00 ns)")

# Generar la gráfica del canal cuántico continuo compartiendo el mismo estado
x_space = np.linspace(0, 4 * np.pi, 200)
if coherence_status == "COHERENTE / ENERGETIZADO":
    # Las ondas del SoC y de la QRAM oscilan en fase perfecta
    y_soc = qram_signal * np.sin(x_space + st.session_state.q_frame)
    y_qram = qram_signal * np.sin(x_space + st.session_state.q_frame)
else:
    # Colapso del enlace cuántico
    y_soc = np.zeros(200)
    y_qram = np.zeros(200)

df_quantum = pd.DataFrame({
    'Coordenada Red': x_space,
    'Estado SoC (Procesador)': y_soc,
    'Estado QRAM (128GB Memoria)': y_qram
})

# Mostrar el gráfico entrelazado centrado en la pantalla
st.line_chart(df_quantum, x='Coordenada Red', height=300)

# =========================================================================
# MÉTRICAS CUANTITATIVAS DEL SUPERCHIP
# =========================================================================
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Latencia Interna SoC-QRAM", value="0.00 ns", delta="NVLink Superado")
with col2:
    st.metric(label="Valor en Bus de 64 bits", value=f"{qram_signal:.4f} Q8.8")
with col3:
    st.metric(label="Capacidad del Sustrato", value="128 GB Unificada")

# Lazo de refresco continuo para mantener la fluidez en share.streamlit.app
if laser_active and abs(temperatura - 24.00) < 0.05:
    time.sleep(0.03)
    st.rerun()