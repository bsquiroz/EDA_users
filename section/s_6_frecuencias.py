import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def mostrar(df: pd.DataFrame):
    st.header("📬 6. Países y Dominios Más Frecuentes")

    # Crear columna de dominio
    df['dominio'] = df['email'].str.extract(r'@([\w\.-]+)')

    # Calcular países y dominios más frecuentes
    paises_frecuentes = df['country'].value_counts().head(10)
    dominios_frecuentes = df['dominio'].value_counts().head(10)

    # --- Gráfico 1: Países ---
    st.subheader("🌍 Países más frecuentes")
    fig, ax = plt.subplots(figsize=(8,4))
    sns.barplot(x=paises_frecuentes.values, y=paises_frecuentes.index, ax=ax, palette="Blues_d")
    ax.set_xlabel("Cantidad de usuarios")
    st.pyplot(fig)

    # --- Gráfico 2: Dominios ---
    st.subheader("💻 Dominios más frecuentes")
    fig, ax = plt.subplots(figsize=(8,4))
    sns.barplot(x=dominios_frecuentes.values, y=dominios_frecuentes.index, ax=ax, palette="OrRd_r")
    ax.set_xlabel("Cantidad de usuarios")
    st.pyplot(fig)

    # --- Top combinaciones país-dominio ---
    st.subheader("🌐 Combinaciones más comunes")
    result = (
        df.groupby(['country', 'dominio'])
        .size()
        .reset_index(name='usuarios')
        .sort_values('usuarios', ascending=False)
        .head(10)
    )
    st.dataframe(result)

    # Explicación breve
    st.markdown("""
    **Interpretación rápida:**
    - Los países y dominios en la parte superior concentran la mayoría de usuarios.
    - Las combinaciones permiten detectar relaciones entre regiones y servicios de correo.
    """)
