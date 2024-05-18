import streamlit as st

st.title("Proyecto Final: Análisis con Machine Learning")

st.subheader("Usabilidad Datos Abiertos")

with st.form("Métricas Dataset"):
   st.text_input("Nombre Dataset:")
   st.number_input(label='Confidencialidad :', min_value = 0, max_value = 10, step = .01, format = "%.2f")


   # Every form must have a submit button.
   submitted = st.form_submit_button("Calcular")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")    
