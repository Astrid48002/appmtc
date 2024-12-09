import streamlit as st

# Título principal
st.markdown("<center><h1>Medidas de Tendencia Central (MTC)</h1></center>", unsafe_allow_html=True)

# Sección de definición general
st.subheader("Definición")
c1, c2 = st.columns([1, 1])

with c1:
    st.markdown("""
    **Las medidas de tendencia central** son valores que resumen un conjunto de datos al identificar un punto central o representativo. 
    Estas medidas permiten interpretar rápidamente los datos y son fundamentales en la estadística descriptiva.
    
    **Principales medidas:**
    - **Media**: Representa el promedio de los datos.
    - **Mediana**: Es el valor central al ordenar los datos.
    - **Moda**: Es el valor más frecuente en el conjunto de datos.
    """)
with c2:
    st.image("img1.png")  # Coloca tu imagen aquí.

st.divider()

# Media
st.markdown(""" (Para el ejemplo que se presentará en las imagénes tener en cuenta: 
Se desea obtener información sobre las edades de los niños que participan en el coro de la iglesia) 
""")
st.subheader("1. La Media")
c1, c2 = st.columns([1, 1])

with c1:
    st.markdown("""
    **La media** es el promedio aritmético de un conjunto de datos. Se calcula sumando todos los valores y dividiéndolos entre el total de observaciones.
    
    **Características importantes:**
    - Se ve afectada por valores extremos (outliers).
    - Es única para cada conjunto de datos.
    """)
with c2:
    st.image("3.png")  # Imagen de apoyo para la media.

# Fórmula de la media
with st.container():
    st.markdown("**Fórmula:**")
    st.latex(r"\bar{x} = \frac{\sum x_i}{N}")
    st.markdown("""
    Donde:
    - \(x_i\): Cada uno de los valores.
    - \(N\): Número total de datos.
    """)

st.divider()

# Mediana
st.subheader("2. La Mediana")
c1, c2 = st.columns([1, 1])

with c1:
    st.markdown("""
    **La mediana** es el valor que divide un conjunto de datos ordenados en dos partes iguales.
    
    **Características importantes:**
    - No se ve afectada por valores extremos.
    - Es única para datos ordenados.
    """)
with c2:
    st.image("4.png")  # Imagen de apoyo para la mediana.

# Fórmula de la mediana
with st.container():
    st.markdown("**Fórmula:**")
    st.markdown("""
    - Si el número total de datos es impar:  
      Mediana = Valor en la posición \((N+1)/2\).
    - Si el número total de datos es par:  
      Mediana = Promedio de los valores en las posiciones \(N/2\) y \((N/2)+1\).
    """)

st.divider()

# Moda
st.subheader("3. La Moda")
c1, c2 = st.columns([1, 1])

with c1:
    st.markdown("""
    **La moda** es el valor que aparece con mayor frecuencia en un conjunto de datos.
    
    **Características importantes:**
    - Puede haber más de una moda (bimodal, multimodal).
    - Es especialmente útil para datos categóricos.
    """)
with c2:
    st.image("5.png")  # Imagen de apoyo para la moda.

# Fórmula de la moda
with st.container():
    st.markdown("**Fórmula:**")
    st.markdown("""
    La moda es el valor que más se repite en el conjunto de datos.  
    - Si solo un valor cumple esta condición, la distribución es unimodal.  
    - Si hay más de un valor con la misma frecuencia máxima, la distribución es bimodal o multimodal.
    
    
    Imágenes tomadas de: GCFAAprendeLibre. (2022). *Media, mediana y moda l Curso de Estadística Básica*. https://www.youtube.com/watch?v=V-3IPTXKZL8""")