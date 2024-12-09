import streamlit as st 

#1) crear las páginas
txts=st.Page("paginas/Definiciones.py",title="Definiciones",default=True, 
icon=":material/description:")
cal=st.Page("paginas/Calculadora.py" ,title="Cálculadora de MTC", 
icon=":material/calculate:")
aps=st.Page("paginas/Aplicaciones.py",title="Evaluación",  
icon=":material/description:")
graphs =st.Page("paginas/Gráficas.py",title="¿Cómo usarlas?",
icon=":material/check:")
ejmp=st.Page("paginas/ejemplos.py",title="Ejemplos",
icon=":material/add:")
pres=st.Page("paginas/presentacion.py",title="¿Quién creó este aplicativo?",
icon=":material/patient_list:")

#crear la navegación 
#pg=st.navigation([txts,inps,ejs])
pg=st.navigation({"Teoría":[txts,graphs,ejmp],"Aplicacion":[cal,aps],"Acerca de":[pres]})



#ejecutar
pg.run()






