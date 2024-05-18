import streamlit as st

st.title("Proyecto Final: Análisis con Machine Learning")

st.subheader("Usabilidad Datos Abiertos")

with st.form("Métricas Dataset"):
   st.text_input("Nombre Dataset:")
   st.number_input('Confidencialidad :', min_value = 0, max_value = 10)
   st.number_input('Relevancia :', min_value = 0, max_value = 10)
   st.number_input('Actualidad :', min_value = 0, max_value = 10)
   st.number_input('Trazabilidad :', min_value = 0, max_value = 10)
   st.number_input('Conformidad :', min_value = 0, max_value = 10)
   st.number_input('Exactitudsintactica :', min_value = 0, max_value = 10)
   st.number_input('Exactitudsemantica :', min_value = 0, max_value = 10)
   st.number_input('Completitud :', min_value = 0, max_value = 10)
   st.number_input('Consistencia :', min_value = 0, max_value = 10)
   st.number_input('Precision :', min_value = 0, max_value = 10)
   st.number_input('Portabilidad :', min_value = 0, max_value = 10)
   st.number_input('Credibilidad :', min_value = 0, max_value = 10)
   st.number_input('Comprensibilidad :', min_value = 0, max_value = 10)
   st.number_input('Accesibilidad :', min_value = 0, max_value = 10)
   st.number_input('Eficiencia :', min_value = 0, max_value = 10)
   st.number_input('Recuperabilidad :', min_value = 0, max_value = 10)
   st.number_input('Disponibilidad :', min_value = 0, max_value = 10)
   st.number_input('Unicidad :', min_value = 0, max_value = 10)

   # Every form must have a submit button.
   submitted = st.form_submit_button("Calcular")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")    
