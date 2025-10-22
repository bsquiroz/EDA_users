import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def mostrar(df: pd.DataFrame):
    st.header("📈 4. Estadísticas Básicas: `age` y `score`")

    st.write("""
    En esta sección calculamos las **medidas estadísticas más importantes** de las columnas
    `age` (edad) y `score` (puntaje):
    - Media  
    - Mediana  
    - Desviación estándar  
    - Rango (máximo - mínimo)
    """)

    # --- Copia limpia y conversión a numérico ---
    df_copy = df.copy()
    df_copy["age"] = pd.to_numeric(df_copy["age"], errors="coerce")
    df_copy["score"] = pd.to_numeric(df_copy["score"], errors="coerce")

    # --- Cálculo de estadísticas ---
    statistics = pd.DataFrame({
        "Media": df_copy[["age", "score"]].mean(),
        "Mediana": df_copy[["age", "score"]].median(),
        "Desviación Estándar": df_copy[["age", "score"]].std(),
        "Rango": df_copy[["age", "score"]].max() - df_copy[["age", "score"]].min()
    }).T  # transponemos para que quede más legible

    st.subheader("📊 Tabla de Estadísticas")
    st.dataframe(statistics.style.format("{:.2f}"))

    # --- Visualización: Boxplots comparativos ---
    st.subheader("📦 Visualización de la Dispersión")

    st.write("""
    Los **boxplots** muestran visualmente cómo se distribuyen los valores.
    Una caja más grande implica mayor dispersión (desviación estándar alta).
    """)

    fig, ax = plt.subplots(1, 2, figsize=(10, 4))
    sns.boxplot(y=df_copy["age"], color="skyblue", ax=ax[0])
    ax[0].set_title("Distribución de Edades (Age)")
    sns.boxplot(y=df_copy["score"], color="salmon", ax=ax[1])
    ax[1].set_title("Distribución de Puntajes (Score)")
    st.pyplot(fig)

    # --- Interpretación textual ---
    st.subheader("🧠 Interpretación de Resultados")

    st.markdown("""
    **Edad (`age`):**  
    - La edad promedio es de aproximadamente **55.9 años**, muy cercana a la mediana (**56**), lo que indica una distribución bastante centrada.  
    - La **desviación estándar alta (~26.4)** y el **rango amplio (~90 años)** muestran que hay una gran variabilidad: hay personas muy jóvenes y muy mayores.

    **Puntaje (`score`):**  
    - La **media (0.50)** y la **mediana (0.51)** son casi iguales, lo que indica una distribución equilibrada sin sesgos marcados.  
    - La **desviación estándar baja (~0.10)**, a pesar de un rango de **0.65**, sugiere que la mayoría de los puntajes están concentrados cerca del promedio, y solo unos pocos valores extremos amplían el rango.
    """)

    st.info("✅ Estas estadísticas ayudan a entender la **distribución y variabilidad** de los datos antes de aplicar modelos o segmentaciones.")
