import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import patches


st.title("¿Cómo usarlas?")
st.write("""
Aunque las medidas de tendencia central (media, mediana y moda) son herramientas fundamentales en el análisis de datos, 
es importante considerar sus ventajas, limitaciones y cuándo es más adecuado utilizarlas. Aquí exploramos estos aspectos 
para ayudarte a elegir la medida correcta según tus necesidades.
""")

st.header("¿En qué me puedo fijar?")
st.write("""
1. La naturaleza de los datos (categóricos, numéricos, continuos u ordinales) determina qué medida es más adecuada.
2. La presencia de valores atípicos puede distorsionar ciertas medidas, como la media.
3. Es importante considerar el propósito del análisis: ¿buscas representar un valor típico o entender la distribución completa?
""")



# Sección 1: Media (Promedio)
st.subheader("Media (Promedio)")
st.write("**Ventajas:**")
st.write("""
- Es fácil de calcular y ampliamente conocida.
- Utiliza toda la información del conjunto de datos, lo que la hace representativa en distribuciones simétricas.
""")
st.write("**Desventajas:**")
st.write("""
- Es sensible a valores atípicos, lo que puede distorsionar el resultado.
- No es adecuada para datos categóricos ni distribuciones muy asimétricas.
""")
st.write("**Tener en cuenta:**")
st.write("""
- Verifica la presencia de valores extremos antes de usarla.
- Es útil para datos numéricos cuando se busca una representación general.

**Ejemplo:**
Salarios de empleados en una empresa
1.5, 1.8, 2, 2.1, 2.2, 50 (en millones de pesos)

La mayoría de los empleados gana entre 1.5 y 2.2 millones de pesos, pero un directivo con un salario de 50 millones eleva la media a 9.27 millones.

**Media:** 9.27 millones

**Mediana:** 2.05 millones *(representa mejor el centro de la distribución)*

**Moda:** No definida 

Problema: Si se usa la media para informar el "salario promedio" de la empresa, se estaría dando una impresión errónea y exagerada de los ingresos reales de los empleados.

""")

# Sección 2: Mediana
st.subheader("Mediana")
st.write("**Ventajas:**")
st.write("""
- No se ve afectada por valores atípicos o distribuciones sesgadas.
- Es adecuada para datos ordinales y distribuciones asimétricas.
""")
st.write("**Desventajas:**")
st.write("""
- No utiliza toda la información del conjunto de datos, solo el valor central.
- Puede ser menos intuitiva de interpretar que la media en algunos contextos.
""")
st.write("**Tener en cuenta:**")
st.write("""
- Úsala cuando hay valores extremos o distribuciones no simétricas.
- Es útil para comparar posiciones relativas dentro de un conjunto de datos.

**Ejemplo:** Hay dos grupos de estudiantes uno de primaria (alrededor de 152 cm) y
el otro de secundaria (alrededor de 172 cm).

La mediana no refleja ninguna tendencia central clara en distribuciones multimodales
como esta.
""")

# Sección 3: Moda
st.subheader("Moda")
st.write("**Ventajas:**")
st.write("""
- Es la única medida adecuada para datos categóricos.
- Puede identificar patrones frecuentes en los datos de forma rápida.
""")
st.write("**Desventajas:**")
st.write("""
- Puede haber más de una moda o no existir una moda única en los datos.
- No siempre es representativa del conjunto completo, especialmente con distribuciones uniformes.
""")
st.write("**Tener en cuenta:**")
st.write("""
- Úsala para datos categóricos o cuando se busca identificar el valor más común.
- En datos numéricos, considera su interpretación limitada frente a la media o mediana.

**Ejemplo:**  
Tiempos de entrega de pedidos: 30.1, 30.2, 30.3, 30.4, 30.5 *(en minutos)*

Cada tiempo de entrega es único, y no hay un valor más frecuente.
 Aquí, calcular la moda carece de sentido práctico porque todos los valores aparecen
una sola vez.
En datos continuos como estos, la moda no aporta ninguna información útil 
sobre la tendencia central.
""")
