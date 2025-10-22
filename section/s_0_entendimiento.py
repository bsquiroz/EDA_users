import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def mostrar(df):
    st.header("🧭 0. Entendimiento de los Datos")

    st.write("""
    Esta sección te permite **conocer la estructura básica del dataset**:
    cómo están distribuidos los valores, cuáles son los promedios,
    y qué tan dispersos están los datos (usando desviación estándar).
    """)

    st.subheader("Viendo toda nuestra data")
    st.dataframe(df.head(10))
    st.dataframe(df.tail(10))

    # --- Mostrar describe ---
    st.subheader("📊 Resumen Estadístico (`df.describe()`)")
    st.dataframe(df.describe())

    st.markdown("""
    **Interpretación rápida de las columnas:**
    - **count** → cuántos datos hay (sin valores nulos)  
    - **mean** → promedio  
    - **std (desviación estándar)** → indica **qué tan dispersos** están los datos respecto al promedio  
    - **min / max** → valores mínimo y máximo  
    - **25%, 50%, 75%** → cuartiles (usados en el boxplot)
    """)

    st.subheader("📦 Visualización: Boxplots para entender la dispersión")
    st.write("""
    Los **boxplots** permiten visualizar la **dispersión** y los **valores atípicos (outliers)**.
    """)

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Edad (`age`)**")
        fig, ax = plt.subplots()
        sns.boxplot(x=df["age"], color='skyblue', ax=ax)
        ax.set_title("Dispersión de las edades")
        ax.set_xlabel("Edad")
        st.pyplot(fig)

    with col2:
        st.write("**Latitud (`latitude`)**")
        fig, ax = plt.subplots()
        sns.boxplot(x=df["latitude"], color='salmon', ax=ax)
        ax.set_title("Dispersión de las latitudes")
        ax.set_xlabel("Latitud")
        st.pyplot(fig)

    st.info("""
    📘 **Conclusión:**
    La desviación estándar mide cuán lejos están los valores del promedio.
    Si los boxplots son **muy extendidos**, los datos varían mucho.
    Si son **compactos**, los datos son más consistentes.
    """)
