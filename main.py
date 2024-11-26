import streamlit as st

st.title("Astrid Bg")
st.caption("Soy estudiante de L. en matemáticas")
st.caption("Otro mensaje")
#titulos
st.title("titulo de nivel 1")
st.header("titulo de nivel 2")
st.subheader("titulo de nivel 3")
st.markdown("""Podemos poner un texto en **negrilla**, en *italica* o ***ambas*** 
 
 Podemos dar color al texto. Por ejemplo, :blue[azul], 
 :violet[rosado]


 """)
#Ecuaciones 

st.latex("a^2+b^2=c^2")

st.image("https://cdn.goconqr.com/uploads/media/image/25214865/desktop_b1661d3d-6ebc-4460-9b51-fb0b58670106.jpeg")
