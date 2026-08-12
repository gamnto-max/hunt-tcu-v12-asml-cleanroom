# src/sim/Q0009_quantum_game.py
# Project: HUNT-QSoC "Continuum" v1.2 (ASML Cleanroom Suite)
# Objective: Streamlit-Native Quantum SoC Game for Laptops Without Mouse

import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. ENTORNO CRÍTICO DE ALTA VELOCIDAD PARA STREAMLIT CLOUD
st.set_page_config(
    page_title="HUNT-QSoC v1.2 - Quantum Game",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estética de laboratorio: Centrado geométrico absoluto y estilo neón para portátiles
st.markdown("""
    <style>
        .stAppDeployButton { display: none; }
        
        /* Contenedor central simétrico para la pantalla del portátil */
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
        
        /* Caja de Consola del Videojuego */
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
        
        /* Centrar y estilizar los botones de disparo para touchpad */
        .stButton button {
            width: 100% !important;
            background-color: #1f3a60 !important;
            color: #00ffaa !important;
            border: 1px solid #00ffaa !important;
            font-weight: bold !important;
            font-family: 'Courier New', monospace !important;
        }
        .stButton button:hover {
            background-color: #00ffaa !important;
            color: #020305 !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🌊 SUBSISTEMA DE SIMULACIÓN GAMING INTERACTIVA")
st.markdown("<p style='color:#8a9a9a; font-size:16px;'><b>DEMOSTRACIÓN TÉCNICA: PHASE WALKER v1.2</b><br>Mitigación en Caliente de Ruido de Transistores de Nvidia en el Bus de la QRAM</p>", unsafe_allow_html=True)

# =========================================================================
# SISTEMA DE RETENCIÓN DE MEMORIA DEL JUEGO (Session State)
# =========================================================================
if "game_qram" not in st.session_state:
    st.session_state.game_qram = 128  # Capacidad base de la QRAM en GB
if "game_phase" not in st.session_state:
    st.session_state.game_phase = 0.0
if "target_channel" not in st.session_state:
    st.session_state.target_channel = 0  # Canal donde aparece el ruido de Nvidia

# Avanzar la fase matemática continuamente para el movimiento de la pantalla
st.session_state.game_phase += 0.15

# Cambiar de forma aleatoria el canal donde ataca el ruido clásico de transistores
if np.random.randint(1, 15) == 1:
    st.session_state.target_channel = np.random.randint(0, 2)

# =========================================================================
# LÓGICA DE CONTROL DEL JUGADOR (Botones ideales para portátiles sin ratón)
# =========================================================================
st.markdown("### 🎛️ Consola de Disparos de Antinodos Hunt (SM-RT Cores)")
col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    if st.button("🌀 ACTIVAR ANTINODO EN CANAL CH0"):
        if st.session_state.target_channel == 0:
            st.session_state.game_qram += 4  # Cancelación exitosa, estabiliza la RAM
            st.toast("¡Teorema de Hunt Aplicado en CH0! Ruido de Nvidia destruido.", icon="🟢")
        else:
            st.session_state.game_qram -= 8  # Desfase por disparo en canal equivocado

with col_btn2:
    if st.button("🌀 ACTIVAR ANTINODO EN CANAL CH1"):
        if st.session_state.target_channel == 1:
            st.session_state.game_qram += 4
            st.toast("¡Teorema de Hunt Aplicado en CH1! Ruido de Nvidia destruido.", icon="🟢")
        else:
            st.session_state.game_qram -= 8

# Degradación pasiva continua de la memoria por interferencia ambiental clásica
st.session_state.game_qram -= 0.5
if st.session_state.game_qram < 0: st.session_state.game_qram = 0
if st.session_state.game_qram > 256: st.session_state.game_qram = 256

# Determinar el estado del reporte técnico según la puntuación de estabilidad
if st.session_state.target_channel == 0:
    ruido_status = "ATAQUE DETECTADO EN CANAL GRÁFICO CH0 (RUIDO CLÁSICO NVIDIA)"
    color_box = "#ff4b4b"
elif st.session_state.target_channel == 1:
    ruido_status = "ATAQUE DETECTADO EN CANAL DE TEXTURAS CH1 (RUIDO CLÁSICO NVIDIA)"
    color_box = "#ff4b4b"
else:
    ruido_status = "BUS EN REPOSO - AUTOPISTA ATÓMICA DE SILICIO-28 COHERENTE"
    color_box = "#00ffaa"

# =========================================================================
# CONSOLA INDUSTRIAL EN EL CENTRO
# =========================================================================
st.markdown(f"""
<div class="console-box" style="border-left: 4px solid {color_box} !important;">
    <div class="console-title" style="color: {color_box} !important;">>>> MONITOR DE INTERCONEXIÓN EN TIEMPO REAL DEL JUEGO</div>
    • Objetivo del Gamer: Presiona el botón del canal bajo ataque para disparar el antinodo geométrico.<br>
    • Estado del Bus   : {ruido_status}<br>
    • Retardo Interno   : 0.00 ns Analítica Combinacional (Transistores de Nvidia Esquivados)<br>
    • Registro de Paridad: SECURE_MATRIX | Bus Nativo de 64 bits Coherente activo
</div>
""", unsafe_allow_html=True)

# =========================================================================
# OSCILOSCOPIO DINÁMICO DEL VIDEOJUEGO CENTRADO
# =========================================================================
st.markdown("### 🌊 Visualización Cinética de las Ondas del Superchip")

x_space = np.linspace(0, 4 * np.pi, 200)

# Canal 00 (Onda Gráfica)
if st.session_state.target_channel == 0:
    y_ch0 = 1.250 * np.sin(x_space - st.session_state.game_phase) + 0.60 * np.cos(x_space * 3.0) # Con ruido
else:
    y_ch0 = 1.250 * np.sin(x_space - st.session_state.game_phase) # Limpio

# Canal 01 (Onda de Memoria)
if st.session_state.target_channel == 1:
    y_ch1 = 0.850 * np.cos(x_space + st.session_state.game_phase) + 0.60 * np.cos(x_space * 3.0) # Con ruido
else:
    y_ch1 = 0.850 * np.cos(x_space + st.session_state.game_phase) # Limpio

df_game_bus = pd.DataFrame({
    'Coordenada Red Cristalina': x_space,
    'Flujo Gráfico CH0 (QGPU)': y_ch0,
    'Flujo Memoria CH1 (QRAM)': y_ch1
})

st.line_chart(df_game_bus, x='Coordenada Red Cristalina', height=300)

# =========================================================================
# MÉTRICAS MAESTRAS EN TIEMPO REAL
# =========================================================================
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Estabilidad Coherente QRAM", value=f"{st.session_state.game_qram:.1f} GB")
with col2:
    st.metric(label="Latencia del Motor de Juego", value="0.00 ns", delta="NVLink Superado")
with col3:
    st.metric(label="Ancho de Bus SoC", value="64-bit Fijo", delta="Precisión Molecular OK")

# Bucle de refresco continuo automatizado para la animación fluida en la nube
time.sleep(0.04)
st.rerun()
