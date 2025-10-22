import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def mostrar(df: pd.DataFrame):
    st.header("🌎 5. Agrupación y Análisis Estadístico por País")

    st.write("""
    En esta sección agrupamos los datos por **país (`country`)** para analizar:
    - Cuántos usuarios hay en cada país  
    - Cuántos tienen edad o score registrados  
    - Promedios de edad y score  

    Usa los controles de abajo para **filtrar o limitar** los países mostrados en los gráficos.
    """)

    # --- Copia y limpieza de datos ---
    df_copy = df.copy()
    df_copy["age"] = pd.to_numeric(df_copy["age"], errors="coerce")
    df_copy["score"] = pd.to_numeric(df_copy["score"], errors="coerce")

    # --- Agrupación ---
    grouped = (
        df_copy.groupby("country")
        .agg(
            usuarios=("id", "count"),
            usuarios_con_edad=("age", "count"),
            usuarios_con_score=("score", "count"),
            edad_promedio=("age", "mean"),
            score_promedio=("score", "mean"),
        )
        .sort_values("usuarios", ascending=False)
    )

    st.subheader("📊 Estadísticas Agrupadas por País")
    st.dataframe(grouped.style.format({
        "edad_promedio": "{:.2f}",
        "score_promedio": "{:.2f}"
    }))

    # --- Selector de países ---
    st.subheader("🎛️ Filtros de Visualización")
    top_n = st.slider(
        "Selecciona cuántos países mostrar (por número de usuarios):",
        min_value=5,
        max_value=min(30, len(grouped)),
        value=10,
        step=1
    )

    top_countries = grouped.head(top_n)

    st.write(f"Mostrando los **{top_n} países con más usuarios**:")

    # --- Visualización 1: Usuarios por país ---
    st.subheader("👥 Distribución de Usuarios por País")
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.barplot(
        x=top_countries.index,
        y=top_countries["usuarios"],
        palette="Blues_d",
        ax=ax
    )
    ax.set_title("Usuarios por País")
    ax.set_ylabel("Cantidad de Usuarios")
    ax.set_xlabel("País")
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

    # --- Visualización 2: Edad promedio vs Score promedio ---
    st.subheader("📊 Comparativa: Edad Promedio vs Score Promedio")
    fig, ax = plt.subplots(figsize=(10, 5))

    width = 0.35
    x = range(len(top_countries))
    ax.bar(x, top_countries["edad_promedio"], width, label="Edad Promedio", color="skyblue")
    ax.bar([i + width for i in x], top_countries["score_promedio"], width, label="Score Promedio", color="salmon")

    ax.set_xticks([i + width/2 for i in x])
    ax.set_xticklabels(top_countries.index, rotation=45)
    ax.set_title("Comparativa de Edad y Score Promedio por País")
    ax.legend()
    st.pyplot(fig)

    # --- Explicación ---
    st.subheader("🧠 Interpretación")
    st.markdown("""
    **Observaciones:**
    - Los países con más usuarios dominan el análisis general.  
    - Las diferencias entre **edad promedio** y **score promedio** pueden indicar patrones demográficos o de comportamiento.  
    - Reducir la cantidad de países ayuda a visualizar mejor las tendencias principales.
    """)
