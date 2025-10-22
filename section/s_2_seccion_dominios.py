import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def mostrar(df):
    # --- SECCIÓN 2: ANÁLISIS DE DOMINIOS DE CORREO ---
    st.header("📧 2. Análisis de Dominios de Correo Electrónico")

    st.write("""
    En esta sección analizaremos **qué tan frecuentes son los distintos dominios**
    (usando la parte del correo después de "@").
    Esto nos ayuda a identificar patrones de usuarios o fuentes de datos similares.
    """)

    # --- Crear copia y extraer dominio ---
    df_copy_domain = df.copy()

    # Extraer la parte del dominio (texto después de "@")
    df_copy_domain['domain'] = df_copy_domain["email"].str.split("@").str[1]

    # Contar ocurrencias por dominio
    repeat_domain = df_copy_domain['domain'].value_counts()

    # Filtrar dominios que aparecen al menos 2 veces
    greater_than_two = repeat_domain[repeat_domain >= 2]

    # Mostrar tabla de dominios con repeticiones
    st.subheader("📊 Dominios que se repiten (al menos 2 veces)")
    st.dataframe(greater_than_two.rename("Cantidad de correos"))

    # --- Agrupar por número de repeticiones ---
    repeat_count = greater_than_two.value_counts().sort_index(ascending=False)

    st.subheader("📈 Recuento de dominios por número de repeticiones")
    st.dataframe(repeat_count.rename("Número de dominios"))

    # --- Gráfico de pastel ---
    st.subheader("🥧 Distribución porcentual de dominios repetidos")

    fig, ax = plt.subplots(figsize=(6,6))
    ax.pie(
        repeat_count,
        labels=repeat_count.index,
        autopct='%1.1f%%',
        startangle=90,
        counterclock=False
    )
    ax.set_title("Distribución de dominios por número de repeticiones")
    st.pyplot(fig)

    # --- Interpretación ---
    st.info("""
    ### 🧠 Interpretación
    Al analizar la **distribución de los dominios de correo electrónico** según su número de repeticiones, se observa que la mayoría aparece solo unas pocas veces.

    Por ejemplo:
    - Los dominios que se repiten **2 o 3 veces** concentran la mayor proporción (más del 70 % del total).
    - Solo un grupo muy pequeño de dominios se repite **más de 5 veces**.

    Esto puede indicar que los usuarios provienen de muchas fuentes distintas o que no hay concentración en un dominio específico.
    """)
