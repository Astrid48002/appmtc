import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import patches

st.title("Veámos algunos ejemplos: ")
st.markdown("Observemos en los ejemplos cómo calcular las MTC con diferentes tipos de datos"
)
st.subheader("1. Datos cualitativos")
c1, c2 = st.columns([3, 1])

with c1:
    st.markdown("""Un restaurante evalúa el sabor favorito de los clientes en sus helados: chocolate, vainilla, fresa, y coco.
    Las frecuencias de respuestas fueron: 
    Chocolate: 35
    Vainilla:50
    Fresa: 40
    Coco: 25
    Para saber qué helado es el favorito deberán calcular la moda, ya que en este caso la media no se puede calcular y la mediana no aporta la información que desean conocer. 


""")

with c2: 
    st.image("6.png")


st.subheader("2. Datos discretos no agrupados: ")
c1, c2 = st.columns([1, 3])

with c1:
    st.image("7.png")

with c2: 
    st.markdown("""Un profesor evalúa las calificaciones (sobre 10) de sus 8 estudiantes: 6, 7, 8, 8, 9, 10, 10, 10.""")
    st.subheader("Datos")

    # Media
    st.subheader("Cálculo de la Media")
    st.latex(r"""
    \text{Fórmula:} \, \bar{x} = \frac{\sum x_i}{n}
    """)
    st.latex(r"""
    \bar{x} = \frac{6 + 7 + 8 + 8 + 9 + 10 + 10 + 10}{8}
    """)
    st.latex(r"""
    \bar{x} = \frac{68}{8} = 8.5
    """)
  # Mediana
st.subheader("Cálculo de la Mediana")
st.latex(r"""
 \text{Ordena los datos:} \, \{6, 7, 8, 8, 9, 10, 10, 10\}
""")
st.latex(r"""
 n = 8 \, \Rightarrow \, \text{Datos centrales: } x_4 = 8, \, x_5 = 9
                    """)
st.latex(r"""
\text{Mediana} = \frac{x_4 + x_5}{2} = \frac{8 + 9}{2} = 8.5
""")

# Moda
st.subheader("Cálculo de la Moda")
st.latex(r"""
\text{La moda es el valor más frecuente.}
""")
st.latex(r"""
\text{Moda} = 10 \, (\text{aparece 3 veces}).
""")

# Resultados finales
st.subheader("Resultados")
st.write("**Media:** 8.5")
st.write("**Mediana:** 8.5")
st.write("**Moda:** 10")

st.markdown("El profesor puede utilizar la media para evaluar el desempeño promedio, la mediana para analizar datos centrados y la moda para identificar calificaciones comunes.")

st.subheader("3. Datos agrupados en intervalos")

st.markdown("Una tienda mide los tiempos que tardan los clientes en hacer compras (en minutos):")

c1, c2 = st.columns([3, 1])


with c1:
     
    st.latex(r""" 
    \begin{array}{|c|c|c|}
    \hline
    \text{Intervalo (min)} & \text{Frecuencia (}f_i\text{)} & \text{Punto medio (}m_i\text{)} \\
    \hline
    0-10 & 5 & 5 \\
    10-20 & 8 & 15 \\
    20-30 & 12 & 25 \\
    30-40 & 10 & 35 \\
    40-50 & 5 & 45 \\
    \hline
    \end{array}
    """)
st.markdown("Para el cálculo de la media usaremos el punto medio y la frecuencia de cada intervalo.")

st.latex(r""" \text{Cálculo de la media:} \quad 
\bar{x} = \frac{\sum f_i m_i}{\sum f_i} = \frac{5(5) + 8(15) + 12(25) + 10(35) + 5(45)}{5 + 8 + 12 + 10 + 5}
""")
st.markdown("**Cálculo de la mediana**")
st.latex(r"""
\text{Datos para calcular la mediana:} \quad 
L = 20, \, F = 13, \, f_m = 12, \, h = 10
""")

st.latex(r"""
\text{Fórmula de la mediana:} \quad 
\text{Mediana} = L + \left(\frac{\frac{N}{2} - F}{f_m}\right) \cdot h
""")
st.markdown("Donde *L* es el límite inferio del intervalo de la mediana, *N* es el total de frecuencia, *f* frecuencia del intervalo de la mediana y *F* es la frecuencia acumulada antes del intervalo de la mediana.")

st.latex(r"""
\text{Mediana} = 20 + \left(\frac{20 - 13}{12}\right) \cdot 10
""")

st.latex(r"""
\text{Mediana} = 20 + \left(\frac{7}{12}\right) \cdot 10 = 20 + 5.83 = 25.83 \, \text{min}
""")

st.latex(r"""
\bar{x} = \frac{25 + 120 + 300 + 350 + 225}{40} = \frac{1020}{40} = 25.5 \, \text{min}
""")

with c2: 
    st.image("8.png")

st.markdown("Imágenes extraidas de ***CANVA***")