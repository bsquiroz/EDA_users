import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def mostrar(df: pd.DataFrame):
    st.header("🌎7️⃣ Top dominios más frecuentes (sin importar país)")

    st.write("""
    En esta sección analizamos los **dominios de correo electrónico más comunes** 
    entre los usuarios del dataset.
    Puedes ajustar el número de dominios mostrados para enfocar el análisis.
    """)

    # --- Asegurar columna de dominio ---
    if "dominio" not in df.columns:
        df["dominio"] = df["email"].str.extract(r'@([\w\.-]+)')

    # --- Selector dinámico ---
    top_n = st.slider("Selecciona cuántos dominios ver:", 5, 50, 10, step=5)

    # --- Calcular top N dominios ---
    top_dominios = (
        df['dominio']
        .value_counts()
        .head(top_n)
        .reset_index()
    )
    top_dominios.columns = ['dominio', 'usuarios']

    # --- Mostrar tabla y gráfico ---
    st.subheader(f"🏆 Top {top_n} dominios más usados")
    st.dataframe(top_dominios)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(top_dominios['dominio'], top_dominios['usuarios'], color='orange')
    ax.set_title(f"Top {top_n} dominios de correo más usados")
    ax.set_xlabel("Dominio")
    ax.set_ylabel("Usuarios")
    plt.xticks(rotation=45, ha='right')
    st.pyplot(fig)
