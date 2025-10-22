import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def mostrar(df: pd.DataFrame):
    st.header("🔗 1️⃣0️⃣ Relación entre Edad y Score")

    st.markdown("""
    En esta sección exploramos la **relación entre la edad y el puntaje (score)** de los usuarios.  
    Esto permite observar si las personas mayores o más jóvenes tienden a tener puntajes más altos o bajos.
    """)

    # --- Asegurar tipos numéricos ---
    df['age'] = pd.to_numeric(df['age'], errors='coerce')
    df['score'] = pd.to_numeric(df['score'], errors='coerce')

    data = df[['age', 'score']].dropna()

    # --- Calcular correlación ---
    corr = data.corr().iloc[0, 1]

    # --- Gráfico de dispersión ---
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.scatter(data['age'], data['score'], color='dodgerblue', alpha=0.6, edgecolors='k')
    ax.set_title(f"Relación entre Edad y Score (r = {corr:.4f})")
    ax.set_xlabel("Edad")
    ax.set_ylabel("Score")
    ax.grid(True, linestyle='--', alpha=0.7)

    st.pyplot(fig)

    # --- Interpretación ---
    st.markdown(f"""
    **Interpretación:**  
    - El coeficiente de correlación entre ambas variables es **{corr:.4f}**.  
    """)
