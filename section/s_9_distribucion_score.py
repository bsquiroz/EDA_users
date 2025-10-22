import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

def mostrar(df: pd.DataFrame):
    st.header("📈 9️⃣ Distribución de Score de Todos los Usuarios")

    st.markdown("""
    En esta sección analizamos cómo se distribuyen los valores de **score** (puntaje) entre todos los usuarios.
    Esto nos ayuda a identificar si los valores están concentrados en un rango o dispersos.
    """)

    # --- Asegurar que 'score' sea numérico ---
    df['score'] = pd.to_numeric(df['score'], errors='coerce')
    scores = df['score'].dropna()

    # --- Histograma ---
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.hist(scores, color='orange', edgecolor='black')
    ax.set_title("Distribución de Puntajes (Score)")
    ax.set_xlabel("Score")
    ax.set_ylabel("Cantidad de Usuarios")
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    st.pyplot(fig)
