import streamlit as st  
import pandas as pd

st.title("Evaluación: ")

#pedir textos: 
nombre=st.text_input("Digite nombre:")

st.header("Pregunta 1")
st.write("¿Cuál de las siguientes medidas de tendencia central no se debe usar en presencia de valores atípicos?")
opciones1 = ["Media", "Mediana", "Moda"]
respuesta_correcta1 = "Media"
respuesta_usuario1 = st.selectbox("Selecciona una opción:", opciones1, key="pregunta1")

if st.button("Enviar respuesta 1", key="boton1"):
    if respuesta_usuario1 == respuesta_correcta1:
        st.success("¡Correcto! La media no es robusta frente a valores atípicos.")
    else:
        st.error("Incorrecto. La respuesta correcta es la media.")

# Pregunta 2
st.header("Pregunta 2")
st.write("¿Cuáles de las siguientes son medidas cualitativas? Selecciona todas las que apliquen:")
opciones2 = ["Media", "Mediana", "Moda", "Frecuencia"]
respuestas_correctas2 = ["Mediana", "Moda"]
respuestas_usuario2 = st.multiselect("Selecciona las opciones:", opciones2, key="pregunta2")

if st.button("Enviar respuesta 2", key="boton2"):
    correctas = [respuesta for respuesta in respuestas_usuario2 if respuesta in respuestas_correctas2]
    incorrectas = [respuesta for respuesta in respuestas_usuario2 if respuesta not in respuestas_correctas2]

    if len(correctas) == len(respuestas_correctas2) and len(incorrectas) == 0:
        st.success("¡Correcto! Has seleccionado todas las medidas cualitativas.")
    else:
        st.error("Incorrecto. Las respuestas correctas son: " + ", ".join(respuestas_correctas2))

st.header("Pregunta 3")
st.write("Dado el siguiente conjunto de datos: [5, 10, 15, 20, 25], ¿cuál es la media?")
respuesta_usuario5 = st.number_input("Ingresa tu respuesta (número):", key="pregunta5")

# Cálculo de la media
datos = [5, 10, 15, 20, 25]
media_correcta = sum(datos) / len(datos)

if st.button("Enviar respuesta 5", key="boton5"):
    if respuesta_usuario5 == media_correcta:
        st.success("¡Correcto! La media es {}".format(media_correcta))
    else:
        st.error("Incorrecto. La respuesta correcta es {}".format(media_correcta))
st.header("Pregunta 4")
st.write("¿Qué son las Medidas de Tendencia Central? Explica brevemente.")
respuesta_usuario6 = st.text_area("Escribe tu respuesta aquí:", key="pregunta6")

if st.button("Enviar respuesta 6", key="boton6"):
    if respuesta_usuario6.strip() != "":
        st.success("¡Gracias por tu respuesta!")
    else:
        st.error("Por favor, escribe una respuesta antes de enviar.")
