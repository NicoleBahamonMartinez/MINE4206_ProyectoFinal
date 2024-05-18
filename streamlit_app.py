import streamlit as st

st.title("Proyecto Final: Análisis con Machine Learning")

st.subheader("Usabilidad Datos Abiertos")

with st.form("Métricas Dataset"):
   st.text_input("Nombre Dataset:")
   st.number_input('confidencialidad :')
   st.number_input('relevancia :')
   st.number_input('actualidad :')
   st.number_input('trazabilidad :')
   st.number_input('conformidad :')
   st.number_input('exactitudSintactica :')
   st.number_input('exactitudSemantica :')
   st.number_input('completitud :')
   st.number_input('consistencia :')
   st.number_input('precision :')
   st.number_input('portabilidad :')
   st.number_input('credibilidad :')
   st.number_input('comprensibilidad :')
   st.number_input('accesibilidad :')
   st.number_input('eficiencia :')
   st.number_input('recuperabilidad :')
   st.number_input('disponibilidad :')
   st.number_input('unicidad :')

   
   slider_val = st.slider("Form slider")
   checkbox_val = st.checkbox("Form checkbox")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("slider", slider_val, "checkbox", checkbox_val)

st.write("Outside the form")    
st.write('Por favor ingrese las métricas de su dataset')

st.text_input("Titulo")