import streamlit as st
import pandas as pd

def mostrar(df: pd.DataFrame):
    st.header("👤 3. Creación de la Columna `full_name`")

    st.write("""
    En esta sección, vamos a **crear una nueva columna** llamada `full_name`, que combina los campos
    `first_name` y `last_name` para obtener el nombre completo de cada persona.
    """)

    st.subheader("🔹 Data original (primeras filas)")
    st.dataframe(df.head())

    # --- Crear columna `full_name` ---
    df_copy = df.copy()
    df_copy["full_name"] = df_copy["first_name"].astype(str) + " " + df_copy["last_name"].astype(str)

    # --- Mover columna `full_name` a la segunda posición ---
    cols = df_copy.columns.tolist()
    cols.insert(1, cols.pop(cols.index("full_name")))
    df_copy = df_copy[cols]

    st.success("✅ Columna `full_name` creada y ubicada después del ID correctamente.")

    # --- Mostrar resultado ---
    st.subheader("📋 DataFrame con la nueva columna")
    st.dataframe(df_copy.head())

    st.info("""
    **Explicación:**
    - Se concatenaron las columnas `first_name` y `last_name` usando un espacio.  
    - Se reordenaron las columnas para que `full_name` quede en la **segunda posición**.  
    - Esto permite una vista más clara al identificar los registros por su nombre completo.
    """)

    return df_copy