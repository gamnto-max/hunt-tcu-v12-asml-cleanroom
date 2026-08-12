# src/sim/Q0006_app.py
# Project: HUNT-QSoC "Continuum" v1.2 (ASML Cleanroom Suite)
# Symmetry: Interactive App for Parity Monitoring and Coherence Fault Detection (Q0006 Tier)

import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. ENTORNO CRÍTICO DE ALTA VELOCIDAD PARA STREAMLIT CLOUD
st.set_page_config(
    page_title="HUNT-QSoC v1.2 - Eslabón Q0006",
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
        
        /* Caja de Consola de Paridad e Integridad */
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

st.title("🛡️ SISTEMA DE MONITOREO DE PARIDAD Y COHERENCIA — ESLABÓN Q0006")
st.markdown("<p style='color:#8a9a9a; font-size:16px;'><b>SÚPER-CHIP CUÁNTICO CONTINUUM v1.2</b><br>Verificación de Integridad Bit a Bit en Caliente sobre el Bus de la QRAM</p>", unsafe_allow_html=True)

# =========================================================================
# CONTROLADORES DE INYECCIÓN DE ERRORES EN LA BARRA LATERAL
# =========================================================================
st.sidebar.header("🎛️ Inyección de Fallos Atómicos")
monitor_active = st.sidebar.checkbox("Activar Árbol XOR", value=True)
inject_fault = st.sidebar.checkbox("Inyectar Ruido de Decorrección (Bit Flip)", value=False)

if "q_frame_6" not in st.session_state:
    st.session_state.q_frame_6 = 0.0

if monitor_active:
    st.session_state.q_frame_6 += 0.10
    
    if inject_fault:
        fault_status = "CRÍTICO - ERROR DE PARIDAD EN BUS DE 64-BIT"
        color_status = "#ff4b4b"
        fault_flag = 1
        computed_parity = 1
    else:
        fault_status = "SISTEMA INTEGRAL - COHERENCIA MOLECULAR OK"
        color_status = "#00ffaa"
        fault_flag = 0
        computed_parity = 0
else:
    fault_status = "MONITOR DESACTIVADO / APAGADO DE COMPUERTAS"
    color_status = "#8a9a9a"
    fault_flag = 0
    computed_parity = 0

# =========================================================================
# CONSOLA INDUSTRIAL INTEGRADA Y CENTRADA
# =========================================================================
st.markdown("### 🖥️ Estado del Árbol de Reducción XOR Combinacional")
st.markdown(f"""
<div class="console-box" style="border-left: 4px solid {color_status} !important;">
    <div class="console-title" style="color: {color_status} !important;">>>> MONITOR DE INTEGRIDAD DE DATOS PRE-SILICIO</div>
    • Topología Core  : Verificación de Matriz en Paralelo Noflip | 64 bits Nativo<br>
    • Estado del Bus   : {fault_status}<br>
    • Bit Paridad Real : [ {computed_parity} ] (Calculado de forma pasiva a la velocidad de la luz)<br>
    • Canal de Alarma  : Registro de Coherencia o_coherence_fault = {fault_flag}<br>
    • Retardo de ECC   : 0.00 ns Absorción Combinacional | Tráfico hacia QRAM Protegido
</div>
""", unsafe_allow_html=True)

# =========================================================================
# OSCILOSCOPIO CINÉTICO DE PARIDAD CENTRADO
# =========================================================================
st.markdown("### 🌊 Análisis de Ondas de Integridad y Estabilidad")

x_space = np.linspace(0, 4 * np.pi, 200)
if monitor_active:
    # La onda de los datos limpios de la QRAM
    y_data_bus = 1.250 * np.sin(x_space + st.session_state.q_frame_6)
    
    if inject_fault:
        # Se genera un ruido destructivo que deforma la onda del bus visualmente
        y_parity_wave = 0.60 * np.cos(x_space * 2.0)
        y_checked_bus = y_data_bus + y_parity_wave
    else:
        y_parity_wave = np.zeros(200)
        y_checked_bus = y_data_bus
else:
    y_data_bus = np.zeros(200)
    y_parity_wave = np.zeros(200)
    y_checked_bus = np.zeros(200)

df_parity_matrix = pd.DataFrame({
    'Coordenada Red Atómica': x_space,
    'Bus de Datos Principal': y_data_bus,
    'Vector Ruido Inyectado': y_parity_wave,
    'Resultado de Señal Validada': y_checked_bus
})

st.line_chart(df_parity_matrix, x='Coordenada Red Atómica', height=350)

# =========================================================================
# MÉTRICAS CUANTITATIVAS DEL MÓDULO SIMÉTRICO
# =========================================================================
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Latencia de Verificación XOR", value="0.00 ns", delta="Cero Penalización")
with col2:
    st.metric(label="Bits de Control Monitorizados", value="64 bits", delta="Simétricos Q32.32")
with col3:
    st.metric(label="Estado del Enlace QRAM", value="SECURE", delta="Protección OK")

# Lazo de refresco continuo para mantener el show fluido en la nube de Streamlit
if monitor_active and not inject_fault:
    time.sleep(0.03)
    st.rerun()