import streamlit as st
import numpy as np
import requests
from pickle import load
from streamlit_lottie import st_lottie

# Cargar el modelo previamente entrenado
with open("../models/random_forest_regression.sav", "rb") as model_file:
    modelo_precio_casas = load(model_file)

# Configuración de la página
st.set_page_config(page_title="Predicción de Precios en Boston", page_icon="🏠", layout="wide")

# Encabezado
st.title("🏡 Aplicación de Predicción de Precios de Viviendas en Boston")
st.write("Usa esta app para estimar el precio de una casa en Boston a partir de sus características.")

# Entrada de datos del usuario
st.subheader("🔎 Introduce los detalles de la propiedad")

# Controles para el usuario
CRIM = st.slider("💥 Tasa de criminalidad per cápita (CRIM)", min_value=0.0, max_value=100.0, value=1.0, step=0.1)
RM = st.slider("🛏️ Promedio de habitaciones por vivienda (RM)", min_value=3.0, max_value=10.0, value=6.0, step=0.1)
DIS = st.slider("📍 Distancia a centros de empleo (DIS)", min_value=1.0, max_value=12.0, value=4.0, step=0.1)
LSTAT = st.slider("📉 % de población con estatus socioeconómico bajo (LSTAT)", min_value=0.0, max_value=40.0, value=10.0, step=0.1)
AGE = st.slider("🏗️ % de casas construidas antes de 1940 (AGE)", min_value=0.0, max_value=100.0, value=50.0, step=1.0)

# Botón para lanzar la predicción
st.markdown("---")
if st.button("🔮 Calcular Precio Estimado"):
    datos_usuario = np.array([[CRIM, RM, DIS, LSTAT, AGE]])
    precio_estimado = modelo_precio_casas.predict(datos_usuario)[0]
    st.success(f"💰 Precio estimado de la propiedad: **${precio_estimado * 1000:.2f} USD**")

st.markdown("---")
