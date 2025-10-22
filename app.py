import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Importar tus secciones
from section import (
    s_0_entendimiento, 
    s_1_limpieza, 
    s_2_seccion_dominios, 
    s_3_nombre_completo, 
    s_4_estadisticas_basicas,
    s_5_agrupacion_paises,
    s_6_frecuencias,
    s_7_frecuencias_barras,
    s_8_continentes,
    s_9_distribucion_score, 
    s_10_relacion_age_score,
)

# ==============================
# 🔧 CONFIGURACIÓN INICIAL
# ==============================
st.set_page_config(
    page_title="📊 Análisis Exploratorio de Datos",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==============================
# 💅 ESTILOS PERSONALIZADOS
# ==============================
st.markdown(
    """
    <style>
    /* Centrar y limitar el ancho del contenido */
    .block-container {
        max-width: 60%;
        margin: auto;
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    /* Centrar títulos y subtítulos */
    h1, h2, h3 {
        text-align: center;
    }

    /* Fondo más limpio */
    body {
        background-color: #fafafa;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ==============================
# 📂 CARGA DE DATOS
# ==============================
@st.cache_data
def load_data(path: str) -> pd.DataFrame:
    """Carga el DataFrame desde un archivo CSV."""
    return pd.read_csv(path)

df = load_data('./usuarios.csv')

# ==============================
# 🧭 NAVEGACIÓN ENTRE SECCIONES
# ==============================
pages = {
    "0️⃣ Entendimiento de los Datos": s_0_entendimiento.mostrar,
    "1️⃣ Limpieza de Datos": s_1_limpieza.mostrar,
    "2️⃣ Análisis de Dominios de Correo Electrónico": s_2_seccion_dominios.mostrar,
    "3️⃣ Creación de la Columna Full Name": s_3_nombre_completo.mostrar,
    "4️⃣ Estadísticas Básicas (Age & Score)": s_4_estadisticas_basicas.mostrar,
    "5️⃣ Agrupación por País": s_5_agrupacion_paises.mostrar,
    "6️⃣ Países y Dominios Más Frecuentes": s_6_frecuencias.mostrar,
    "7️⃣ Top dominios más frecuentes (sin importar país)": s_7_frecuencias_barras.mostrar,
    "8️⃣ Proporción por Continente": s_8_continentes.mostrar,
    "9️⃣ Distribución de Score": s_9_distribucion_score.mostrar,
    "1️⃣0️⃣ Relación entre Edad y Score": s_10_relacion_age_score.mostrar,
}

st.sidebar.title("🔍 Navegación")
selected_page = st.sidebar.radio("Selecciona una sección:", list(pages.keys()))

# ==============================
# 🚀 EJECUCIÓN DE LA SECCIÓN
# ==============================
st.title("📊 Análisis Exploratorio de Datos")
pages[selected_page](df)
