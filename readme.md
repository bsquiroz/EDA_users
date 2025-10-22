# 📊 Análisis Exploratorio de Datos — `usuarios.csv`

Este proyecto realiza un **Análisis Exploratorio de Datos (EDA)** sobre un conjunto de información de usuarios, combinando el uso de **pandas** 🐼 para manipulación y **matplotlib** 🎨 para visualización, todo dentro de una **app interactiva en Streamlit** 🚀.

---

## 🧩 Descripción General

- **Archivo analizado:** `usuarios.csv`
- **Propósito:** Entender patrones demográficos y de comportamiento de los usuarios.
- **Tecnologías:**  
  🐍 Python · 📘 Pandas · 📊 Matplotlib · 🌐 Streamlit

---

## 📁 Índice

1️⃣ [Gestión de valores nulos](#1️⃣-gestión-de-nulos)  
2️⃣ [Exploración de dominios](#2️⃣-exploración-de-dominios)  
3️⃣ [Creación de columna `full_name`](#3️⃣-creación-de-nuevas-columnas)  
4️⃣ [Estadística descriptiva](#4️⃣-estadística-descriptiva)  
5️⃣ [Agrupación por país](#5️⃣-agrupación-y-análisis-por-categoría)  
6️⃣ [Países y dominios más frecuentes](#6️⃣-selección-y-filtrado)  
7️⃣ [Gráfico de barras — Top dominios](#7️⃣-gráfico-de-barras)  
8️⃣ [Gráfico circular — Continentes](#8️⃣-gráfico-circular-pie-chart)  
9️⃣ [Histograma — Distribución de scores](#9️⃣-histograma)  
🔟 [Diagrama de dispersión — Edad vs Score](#🔟-diagrama-de-dispersión)

---

## 🧮 Tareas con Pandas

### 1️⃣ Gestión de Nulos

**Habilidad:** Limpieza de datos  
**Instrucción:** Identificar y manejar valores nulos en `age` y otras columnas críticas.  
🔗 Sección: `s_1_limpieza.py`

---

### 2️⃣ Exploración de Dominios

**Habilidad:** Transformación y conteo  
**Instrucción:** Extraer el dominio del correo (`email`) y calcular su frecuencia, visualizando los resultados en un gráfico de torta.  
🔗 Sección: `s_2_seccion_dominios.py`

---

### 3️⃣ Creación de Nuevas Columnas

**Habilidad:** Ingeniería de datos  
**Instrucción:** Combinar `first_name` y `last_name` en una nueva columna llamada `full_name`.  
🔗 Sección: `s_3_nombre_completo.py`

---

### 4️⃣ Estadística Descriptiva

**Habilidad:** Resumen de datos  
**Instrucción:** Calcular media, mediana, desviación estándar y rango para `age` y `score`.  
🔗 Sección: `s_4_estadisticas_basicas.py`

---

### 5️⃣ Agrupación y Análisis por Categoría

**Habilidad:** Agrupación con `groupby()`  
**Instrucción:** Agrupar por país (`country`) para obtener promedio de edad, score y cantidad de usuarios.  
🔗 Sección: `s_5_agrupacion_paises.py`

---

### 6️⃣ Selección y Filtrado

**Habilidad:** Conteo y ordenamiento  
**Instrucción:** Identificar los países y dominios más frecuentes.  
🔗 Sección: `s_6_frecuencias.py`

---

## 📈 Tareas con Matplotlib

### 7️⃣ Gráfico de Barras

**Habilidad:** Visualización dinámica  
**Instrucción:** Mostrar los dominios de correo más frecuentes con opción para ajustar el número de dominios (Top N).  
🔗 Sección: `s_7_frecuencias_barras.py`

---

### 8️⃣ Gráfico Circular (Pie Chart)

**Habilidad:** Visualización de proporciones  
**Instrucción:** Mostrar la proporción de usuarios por continente según su país.  
🔗 Sección: `s_8_continentes.py`

---

### 9️⃣ Histograma

**Habilidad:** Distribución de frecuencias  
**Instrucción:** Visualizar cómo se distribuye el `score` de los usuarios.  
🔗 Sección: `s_9_distribucion_score.py`

---

### 🔟 Diagrama de Dispersión

**Habilidad:** Correlación entre variables  
**Instrucción:** Explorar la relación entre `age` y `score` y calcular el coeficiente de correlación.  
🔗 Sección: `s_10_dispersion_age_score.py`

---

## ⚙️ Instalación y Ejecución

🧩 1. Crear el entorno virtual

```bash
python -m venv venv
```

---

▶️ 2. Activar el entorno virtual

En Windows:

```bash
venv\Scripts\activate
```

En macOS / Linux:

```bash
source venv/bin/activate
```

💡 Nota:
Para desactivar el entorno virtual en cualquier momento:

```bash
deactivate
```

---

📦 3. Instalar dependencias

Asegúrate de estar dentro del entorno virtual antes de ejecutar:

```bash
pip install -r requirements.txt
```

---

🚀 4. Ejecutar la aplicación

```bash
streamlit run app.py
```
