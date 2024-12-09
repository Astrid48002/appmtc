import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import patches
from collections import Counter 

st.title("Cálculadora de MTC para *Datos discretos no agrupados*")
st.write("Ingresa tus datos discretos no agrupados para calcular las medidas de tendencia central.")

# Entrada de datos
datos_input = st.text_area("Introduce tus datos separados por comas (ejemplo: 1, 2, 2, 3, 4)", "")

if datos_input:
    try:
        # Convertir los datos en una lista de enteros
        datos = list(map(int, datos_input.split(",")))
        st.write("Tus datos:", datos)

        # Calcular la media
        media = np.mean(datos)
        st.write(f"Media: {media:.2f}")

        # Calcular la mediana
        mediana = np.median(datos)
        st.write(f"Mediana: {mediana:.2f}")

        # Calcular la moda
        conteo = Counter(datos)
        moda = [key for key, value in conteo.items() if value == max(conteo.values())]
        if len(moda) == len(datos):  # Si todos los valores tienen la misma frecuencia
            st.write("Moda: No hay una moda específica (todos los datos tienen la misma frecuencia).")
        else:
            st.write(f"Moda: {', '.join(map(str, moda))}")

    except ValueError:
        st.error("Por favor, asegúrate de ingresar solo números enteros separados por comas.")

else:
    st.write("Por favor, ingresa los datos para calcular las medidas.")