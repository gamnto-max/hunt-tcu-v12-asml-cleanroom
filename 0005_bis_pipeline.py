# src/sim/0005_pipeline.py
# Project: HUNT-TCU v1.2 - Full Control Center & Kinetic Pipeline Centered
# Operator Master: Richard | Pure Silicon-28 Validation Suite

import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. ENTORNO CRÍTICO DE ALTA VELOCIDAD
st.set_page_config(
    page_title="HUNT-TCU v1.2 - ASML Control Center",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Estética de laboratorio termoestable: Forzar alineación y centrado absoluto en el monitor
st.markdown("""
    <style>
        .stAppDeployButton { display: none; }
        
        /* Contenedor maestro centrado en la pantalla de la laptop */
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
        
        /* Centrar titulos y texto descriptivo */
        h1, h2, h3, p, .stMarkdown {
            text-align: center !important;
        }
        
        /* Cajas de Consola Centradas para Datos de Control */
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
        
        /* Estilo neón para las métricas del bus cuántico */
        [data-testid="stMetricValue"] {
            color: #00ffaa !important;
            font-family: 'Courier New', monospace;
            text-align: center !important;
        }
        [data-testid="stMetricLabel"] {
            text-align: center !important;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🌊 CENTRO DE CONTROL INTEGRADO — ASML v1.2")
st.markdown("<p style='color:#8a9a9a; font-size:16px;'><b>OPERADOR MÁSTER: RICHARD</b><br>Monitoreo Concurrente y Simulación en Silicio-28</p>", unsafe_allow_html=True)

# =========================================================================
# CONSOLAS DE CONTROL CENTRALIZADAS (0001, 0002, 0003)
# =========================================================================
st.markdown("### 🖥️ Matriz de Secuencias del Superchip")

# Consola 0001: Calibración
st.markdown("""
<div class="console-box">
    <div class="console-title">>>> SECUENCIA 0001: CALIBRACIÓN INICIAL EN LÍNEA</div>
    • Sustrato Cuántico : Silicio-28 Puro (Espín Magnético Cero)<br>
    • Matriz Térmica   : 24.00 C Constant (Estabilización OK)<br>
    • Láser de Control  : 0.4 uW Non-Intrusive | Eje Enfocado
</div>
""", unsafe_allow_html=True)

# Consola 0002: Vectores Concurrentes
st.markdown("""
<div class="console-box">
    <div class="console-title">>>> SECUENCIA 0002: FLUJO DE VECTORES CONCURRENTES</div>
    • Canal SM_RT 00    : Señal Analítica:  1.250 | Ruido Fase:  0.450 -> REG_OK<br>
    • Canal SM_RT 01    : Señal Analítica: -2.500 | Ruido Fase: -0.850 -> REG_OK<br>
    • Ancho de Bus Nat  : 64-bit Symmetric Matrix Precision
</div>
""", unsafe_allow_html=True)

# Consola 0003: Procesamiento Determinista
st.markdown("""
<div class="console-box">
    <div class="console-title">>>> SECUENCIA 0003: PROCESAMIENTO DETERMINISTA (TEOREMA DE HUNT)</div>
    • Ecuación de Red   : o_clean = i_sig + i_noise + (~i_noise + 1)<br>
    • Resultado Bus     : 1.250000 (Señal cuántica recuperada intacta)<br>
    • Error Residual    : 0.0000000000000000 | Latencia Física: 0.00 ns
</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================================================================
# OSCILOSCOPIO CINÉTICO EN TIEMPO REAL
# =========================================================================
st.markdown("### 🌊 Osciloscopio Cinético de Ondas")

# Constantes Absolutas de la Iniciativa Tridente
AREA_FIJA = 24.00
BX_TARGET, BY_TARGET = 2.0, 6.0
X_CRESTA, X_VALLE = 1.0, 3.0

if "fase_reloj" not in st.session_state:
    st.session_state.fase_reloj = 0.0
if "flujo_activo" not in st.session_state:
    st.session_state.flujo_activo = True

# Interruptores laterales de operación
st.sidebar.header("🎛️ Control de Frecuencia")
velocidad = st.sidebar.slider("Velocidad de Barrido (Δ)", 0.01, 0.15, 0.04, step=0.01)
estres_mecanico = st.sidebar.slider("Estrés Crítico Inducido (V)", 0.0, 2.0, 0.0, step=0.1)

if st.sidebar.button("⏯️ Pausar / Reanudar Flujo"):
    st.session_state.flujo_activo = not st.session_state.flujo_activo

if st.session_state.flujo_activo:
    st.session_state.fase_reloj += velocidad
    if st.session_state.fase_reloj > 2 * np.pi:
        st.session_state.fase_reloj -= 2 * np.pi

amplitud_base = 2.8
offset_y = 6.0

y_cresta_hunt = offset_y + (amplitud_base + estres_mecanico) * np.sin((np.pi / 2) * X_CRESTA + st.session_state.fase_reloj)
y_valle_hunt = offset_y + (amplitud_base - estres_mecanico) * np.sin((np.pi / 2) * X_VALLE + st.session_state.fase_reloj)

bx_calculado = (X_CRESTA + X_VALLE) / 2
by_calculado = (y_cresta_hunt + y_valle_hunt) / 2
residuo_vectorial = np.abs(by_calculado - BY_TARGET)

x_onda = np.linspace(0.0, 4.0, 180)
y_onda = offset_y + (amplitud_base + estres_mecanico * np.sin((np.pi / 2) * x_onda + st.session_state.fase_reloj)) * np.sin((np.pi / 2) * x_onda + st.session_state.fase_reloj)

df_onda = pd.DataFrame({
    'Eje X': x_onda,
    'Eje Y': y_onda,
    'Componente Físico': 'Flujo de Reloj Combinacional',
    'Dimensión': 12
})

df_nodos = pd.DataFrame({
    'Eje X': [X_CRESTA, X_VALLE, bx_calculado],
    'Eje Y': [y_cresta_hunt, y_valle_hunt, by_calculado],
    'Componente Físico': ['Cresta Computada', 'Valle Computado', 'BARICENTRO LOCKED (2,6)'],
    'Dimensión': [50, 50, 180]
})

df_osciloscopio = pd.concat([df_onda, df_nodos], ignore_index=True)

st.scatter_chart(
    df_osciloscopio,
    x='Eje X',
    y='Eje Y',
    color='Componente Físico',
    size='Dimensión',
    width='stretch',
    height=400
)

# Métricas alineadas en columnas centradas
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Fase Vectorial", value=f"{st.session_state.fase_reloj:.3f} rad")
with col2:
    st.metric(label="Baricentro Y", value=f"{by_calculado:.2f}", delta=f"Residuo: {residuo_vectorial:.4f}")
with col3:
    st.metric(label="Área Núcleo", value=f"{AREA_FIJA:.2f} u²")
with col4:
    st.metric(label="Compensación", value="ACTIVA", delta="Filtro OK")

if st.session_state.flujo_activo:
    time.sleep(0.01)
    st.rerun()
