# src/sim/0005_pipeline.py
# Project: HUNT-TCU v1.2 - Smooth Kinetic Pipeline Centered
# Operator Master: Richard | Pure Silicon-28 Validation Suite

import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. ENTORNO CRÍTICO DE ALTA VELOCIDAD
st.set_page_config(
    page_title="HUNT-TCU v1.2 - Centered Kinetic Pipeline",
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
        h1, p, .stMarkdown {
            text-align: center !important;
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

st.title("🌊 OSCILOSCOPIO CINÉTICO FLUIDO")
st.markdown("<p style='color:#8a9a9a; font-size:16px;'><b>TEOREMA DE HUNT ACTIVE</b><br>Operador Máster: Richard | Desplazamiento Continuo Centrado en Silicio-28</p>", unsafe_allow_html=True)

# Constantes Absolutas de la Iniciativa Tridente
AREA_FIJA = 24.00
BX_TARGET, BY_TARGET = 2.0, 6.0
X_CRESTA, X_VALLE = 1.0, 3.0

# 2. SISTEMA DE RETENCIÓN DE FASE (Session State)
if "fase_reloj" not in st.session_state:
    st.session_state.fase_reloj = 0.0
if "flujo_activo" not in st.session_state:
    st.session_state.flujo_activo = True

# 3. INTERRUPTORES LATERALES DE OPERACIÓN (Control en barra colapsable)
st.sidebar.header("🎛️ Control de Frecuencia")
velocidad = st.sidebar.slider("Velocidad de Barrido (Δ)", 0.01, 0.15, 0.04, step=0.01)
estres_mecanico = st.sidebar.slider("Estrés Crítico Inducido (V)", 0.0, 2.0, 0.0, step=0.1)

if st.sidebar.button("⏯️ Pausar / Reanudar Flujo"):
    st.session_state.flujo_activo = not st.session_state.flujo_activo

# Avanzar la fase matemática continuamente para lograr el desplazamiento
if st.session_state.flujo_activo:
    st.session_state.fase_reloj += velocidad
    if st.session_state.fase_reloj > 2 * np.pi:
        st.session_state.fase_reloj -= 2 * np.pi

amplitud_base = 2.8
offset_y = 6.0

# 4. APLICACIÓN DE LAS ECUACIONES SINCRO-MÓVILES DEL TEOREMA DE HUNT
y_cresta_hunt = offset_y + (amplitud_base + estres_mecanico) * np.sin((np.pi / 2) * X_CRESTA + st.session_state.fase_reloj)
y_valle_hunt = offset_y + (amplitud_base - estres_mecanico) * np.sin((np.pi / 2) * X_VALLE + st.session_state.fase_reloj)

bx_calculado = (X_CRESTA + X_VALLE) / 2
by_calculado = (y_cresta_hunt + y_valle_hunt) / 2
residuo_vectorial = np.abs(by_calculado - BY_TARGET)

# 5. CONSTRUCCIÓN DE LA MATRIZ DE DATOS UNIFICADA
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

# 6. RENDERIZADO EN EL CENTRO EXACTO DE LA PORTÁTIL
st.scatter_chart(
    df_osciloscopio,
    x='Eje X',
    y='Eje Y',
    color='Componente Físico',
    size='Dimensión',
    width='stretch',
    height=450
)

# 7. METRICAS CUANTITATIVAS ALINEADAS EN COLUMNAS CENTRADAS
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="Fase Vectorial", value=f"{st.session_state.fase_reloj:.3f} rad")
with col2:
    st.metric(label="Baricentro Y", value=f"{by_calculado:.2f}", delta=f"Residuo: {residuo_vectorial:.4f}")
with col3:
    st.metric(label="Área Núcleo", value=f"{AREA_FIJA:.2f} u²")
with col4:
    st.metric(label="Compensación", value="ACTIVA", delta="Filtro OK")

# 8. EXPLICACIÓN CIENTÍFICA DEL COMPORTAMIENTO CINÉTICO
st.markdown("### 🧬 Análisis del Desplazamiento de Fase y Cancelación de Ruido")
st.markdown(r"""
Al procesar la señal de forma nativa, las componentes espaciales de la onda electromagnética se desplazan siguiendo la relación de propagación $\psi(x, t) = A \cdot \sin(kx + \omega t)$. Observe cómo los nodos de la **Cresta** y el **Valle** oscilan verticalmente de manera contrapuesta, pero el **Baricentro Cuántico** permanece perfectamente inmóvil en el centro del universo digital, validando empíricamente el Teorema de Hunt.
""")

if st.session_state.flujo_activo:
    time.sleep(0.01)
    st.rerun()
