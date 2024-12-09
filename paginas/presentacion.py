import streamlit as st 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import patches

st.title("¿Quién creó este aplicativo? ")
c1, c2 = st.columns([3, 1])

with c1:
    st.markdown("""¡Hola!, mi nombre es Astrid Fernanda Bohórquez Gómez, con código de estudiante 2200234 de la carrera Lic. en matemáticas de 7mo semestre. 
    Este aplicativo lo puedes usar como estudiante para repasar tus concocimientos sobre MTC o para profesor como recurso interactivo donde puedes reforsar y evaluar el aprendizaje de tus estudiantes. Puedes enviar cualquier retroalimentación a astridbg48@gmail.com""")
with c2: 
    st.image("IMG_5726.PNG")
