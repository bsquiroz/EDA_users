import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt

def mostrar(df):
    st.header("🧹 1. Limpieza de Datos: Gestión de Nulos")

    st.write("""
    Antes de analizar o modelar los datos, es esencial revisar si hay valores **nulos o faltantes**.
    """)

    # --- Conteo de nulos ---
    st.subheader("📊 Conteo de Nulos por Columna")
    null_counts = df.isnull().sum().reset_index()
    null_counts.columns = ["Columna", "Cantidad de Nulos"]
    st.dataframe(null_counts)

    # --- Porcentaje de nulos ---
    st.subheader("📈 Porcentaje de Nulos (%)")
    null_percentage = (df.isnull().mean() * 100).reset_index()
    null_percentage.columns = ["Columna", "Porcentaje (%)"]
    st.dataframe(null_percentage.style.format({"Porcentaje (%)": "{:.2f}"}))

    # --- Visualización ---
    st.subheader("📉 Visualización de Nulos")
    fig, ax = plt.subplots()
    sns.barplot(x=null_counts["Columna"], y=null_counts["Cantidad de Nulos"], palette="coolwarm", ax=ax)
    ax.set_title("Cantidad de valores nulos por columna")
    st.pyplot(fig)

    # --- Acciones ---
    st.subheader("🧭 Acciones para gestionar nulos")
    accion = st.radio(
        "Selecciona una acción:",
        ["No hacer nada (solo observar)",
         "Eliminar filas con nulos",
         "Rellenar con la media (numéricos)",
         "Rellenar con cero"]
    )

    df_clean = df.copy()

    if accion == "Eliminar filas con nulos":
        df_clean = df.dropna()
        st.success("✅ Se eliminaron todas las filas que contenían valores nulos.")
    elif accion == "Rellenar con la media (numéricos)":
        df_clean = df.fillna(df.mean(numeric_only=True))
        st.success("✅ Los valores nulos fueron reemplazados por la media de cada columna numérica.")
    elif accion == "Rellenar con cero":
        df_clean = df.fillna(0)
        st.success("✅ Los valores nulos fueron reemplazados con 0.")
    else:
        st.info("👀 No se ha aplicado ningún cambio. Solo observación.")

    st.subheader("🧾 DataFrame Limpio (Vista Previa)")
    st.dataframe(df_clean.head())

    st.subheader("📋 Resumen después de limpieza")
    st.dataframe(df_clean.describe())
