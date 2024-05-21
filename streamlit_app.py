import streamlit as st
import time as t
# import joblib
import numpy as np

def predict(data):
    # clf = joblib.load(“rf_model.sav”)
    # return clf.predict(data)
    return sum(data)/17

# col1, col2 = st.columns([0.25,0.10])
# col1.image('MINE4206_ProyectoFinal\images\mintic.png')


st.title("Proyecto Final: Análisis con Machine Learning")

st.subheader("Usabilidad Datos Abiertos")

with st.form("Métricas Dataset", clear_on_submit = False):

  Nombre = st.text_input("Nombre Dataset:")
  c1, c2, c3 = st.columns(3)
  
  metricas = [None] * 18
  with c1:
    metricas[0] = st.number_input('Confidencialidad :', min_value = 0.0, max_value = 10.0, format = "%.2f", step = 0.01,  )
    metricas[1] = st.number_input('Relevancia :', min_value = 0.0, max_value = 10.0, format = "%.2f", step = 0.01)
    metricas[2] = st.number_input('Actualidad :', min_value = 0.0, max_value = 10.0, format = "%.2f", step = 0.01)
    metricas[3] = st.number_input('Trazabilidad :', min_value = 0.0, max_value = 10.0, format = "%.2f", step = 0.01)
    metricas[4] = st.number_input('Conformidad :', min_value = 0.0, max_value = 10.0, format = "%.2f", step = 0.01)
    metricas[5] = st.number_input('Exactitud Sintactica :', min_value = 0.0, max_value = 10.0, format = "%.2f", step = 0.01)

  with c2:
    metricas[6] = st.number_input('Exactitud Semantica :', min_value = 0.0, max_value = 10.0, format = "%.2f", step = 0.01)
    metricas[7] = st.number_input('Completitud :', min_value = 0.0, max_value = 10.0, format = "%.2f", step = 0.01)
    metricas[8] = st.number_input('Consistencia :', min_value = 0.0, max_value = 10.0, format = "%.2f", step = 0.01)
    metricas[9] = st.number_input('Precision :', min_value = 0.0, max_value = 10.0, format = "%.2f", step = 0.01)
    metricas[10] = st.number_input('Portabilidad :', min_value = 0.0, max_value = 10.0, format = "%.2f", step = 0.01)
    metricas[11] = st.number_input('Credibilidad :', min_value = 0.0, max_value = 10.0, format = "%.2f", step = 0.01)

  with c3:
    metricas[12] = st.number_input('Comprensibilidad :', min_value = 0.0, max_value = 10.0, format = "%.2f", step = 0.01)
    metricas[13] = st.number_input('Accesibilidad :', min_value = 0.0, max_value = 10.0, format = "%.2f", step = 0.01)
    metricas[14] = st.number_input('Eficiencia :', min_value = 0.0, max_value = 10.0, format = "%.2f", step = 0.01)
    metricas[15] = st.number_input('Recuperabilidad :', min_value = 0.0, max_value = 10.0, format = "%.2f", step = 0.01)
    metricas[16] = st.number_input('Disponibilidad :', min_value = 0.0, max_value = 10.0, format = "%.2f", step = 0.01)
    metricas[17] = st.number_input('Unicidad :', min_value = 0.0, max_value = 10.0, format = "%.2f", step = 0.01)

  submitted = st.form_submit_button("Calcular")

  # Every form must have a submit button.
  if 'countSubmitted' not in st.session_state:
    st.session_state.countSubmitted = 0
    
if submitted:
    if Nombre == '':
        st.error('Llene todos los campos antes de enviar')
    elif (sum(metricas) == 0 and st.session_state.countSubmitted == 0):
       st.warning('Verifique que todos los valores de las métricas hayan sido ingresados')
       st.session_state.countSubmitted += 1
    else:
        with st.spinner("Processing your text...."):
            t.sleep(1)
            try:
                result_df = predict(np.array(metricas))
                st.success("✅ Done!")
                st.write('El dataset '+ Nombre + ' tiene un incentivo de uso de ' + str(result_df))   
            except:
                st.error("Something happened", icon="🚨")
            


