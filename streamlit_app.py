import streamlit as st
import time as t
import numpy as np
import pickle
from sklearn.preprocessing import FunctionTransformer
import pandas as pd
import datetime

def seleccionar_columnas(X):
    return X[['confidencialidad', 'relevancia', 'actualidad', 'trazabilidad', 'conformidad',
              'exactitudSintactica', 'exactitudSemantica', 'completitud', 'consistencia',
              'precision', 'portabilidad', 'credibilidad', 'comprensibilidad', 'accesibilidad',
              'eficiencia', 'recuperabilidad', 'disponibilidad', 'unicidad']]
selector_columnas = FunctionTransformer(seleccionar_columnas)

class MetadataEvaluator:
    def __init__(self, model_path):
        with open(model_path, 'rb') as file:
            self.loaded_pipeline = pickle.load(file)
    
    def predict(self, diccionarioCalificaciones):
        calificacionIncentivoUso = self.loaded_pipeline.predict(diccionarioCalificaciones)[0] * 10
        return round(calificacionIncentivoUso, 2)

class StreamlitApp:
    def __init__(self):
        self.evaluator = MetadataEvaluator('model/final_model.pkl')
        self.metricas = [None] * 18

    def run(self):
        col1, col2 = st.columns([0.25,0.10])
        col1.image('./images/mintic.png')
        st.title("Proyecto Final: Análisis con Machine Learning")
        st.subheader("Usabilidad Datos Abiertos")
        self.render_forms()

    def render_forms(self):
        self.render_manual_form()
        self.render_csv_form()

    def render_manual_form(self):
        with st.form("Métricas Dataset", clear_on_submit=False):
            Nombre = st.text_input("Nombre Dataset:")
            self.render_metrics_input()

            submitted = st.form_submit_button("Calcular")
            if 'countSubmitted' not in st.session_state:
                st.session_state.countSubmitted = 0

            if submitted:
                self.process_manual_submission(Nombre)

    def render_metrics_input(self):
        c1, c2, c3 = st.columns(3)
        with c1:
            self.metricas[0] = st.number_input('Confidencialidad :', min_value=0.0, max_value=10.0, format="%.2f", step=0.01)
            self.metricas[1] = st.number_input('Relevancia :', min_value=0.0, max_value=10.0, format="%.2f", step=0.01)
            self.metricas[2] = st.number_input('Actualidad :', min_value=0.0, max_value=10.0, format="%.2f", step=0.01)
            self.metricas[3] = st.number_input('Trazabilidad :', min_value=0.0, max_value=10.0, format="%.2f", step=0.01)
            self.metricas[4] = st.number_input('Conformidad :', min_value=0.0, max_value=10.0, format="%.2f", step=0.01)
            self.metricas[5] = st.number_input('Exactitud Sintactica :', min_value=0.0, max_value=10.0, format="%.2f", step=0.01)
        with c2:
            self.metricas[6] = st.number_input('Exactitud Semantica :', min_value=0.0, max_value=10.0, format="%.2f", step=0.01)
            self.metricas[7] = st.number_input('Completitud :', min_value=0.0, max_value=10.0, format="%.2f", step=0.01)
            self.metricas[8] = st.number_input('Consistencia :', min_value=0.0, max_value=10.0, format="%.2f", step=0.01)
            self.metricas[9] = st.number_input('Precisión :', min_value=0.0, max_value=10.0, format="%.2f", step=0.01)
            self.metricas[10] = st.number_input('Portabilidad :', min_value=0.0, max_value=10.0, format="%.2f", step=0.01)
            self.metricas[11] = st.number_input('Credibilidad :', min_value=0.0, max_value=10.0, format="%.2f", step=0.01)
        with c3:
            self.metricas[12] = st.number_input('Comprensibilidad :', min_value=0.0, max_value=10.0, format="%.2f", step=0.01)
            self.metricas[13] = st.number_input('Accesibilidad :', min_value=0.0, max_value=10.0, format="%.2f", step=0.01)
            self.metricas[14] = st.number_input('Eficiencia :', min_value=0.0, max_value=10.0, format="%.2f", step=0.01)
            self.metricas[15] = st.number_input('Recuperabilidad :', min_value=0.0, max_value=10.0, format="%.2f", step=0.01)
            self.metricas[16] = st.number_input('Disponibilidad :', min_value=0.0, max_value=10.0, format="%.2f", step=0.01)
            self.metricas[17] = st.number_input('Unicidad :', min_value=0.0, max_value=10.0, format="%.2f", step=0.01)

    def process_manual_submission(self, Nombre):
        metricas_modelo = {
            'confidencialidad': self.metricas[0], 
            'relevancia': self.metricas[1], 
            'actualidad': self.metricas[2], 
            'trazabilidad': self.metricas[3],
            'conformidad': self.metricas[4], 
            'exactitudSintactica': self.metricas[5], 
            'exactitudSemantica': self.metricas[6],
            'completitud': self.metricas[7], 
            'consistencia': self.metricas[8], 
            'precision': self.metricas[9], 
            'portabilidad': self.metricas[10],
            'credibilidad': self.metricas[11], 
            'comprensibilidad': self.metricas[12], 
            'accesibilidad': self.metricas[13], 
            'eficiencia': self.metricas[14],
            'recuperabilidad': self.metricas[15], 
            'disponibilidad': self.metricas[16], 
            'unicidad': self.metricas[17]
        }
        metricas_modelo = pd.DataFrame([metricas_modelo])

        if Nombre == '':
            st.error('Llene todos los campos antes de enviar')
        elif sum(metricas_modelo[metricas_modelo.columns].sum(axis=1)) == 0 and st.session_state.countSubmitted == 0:
            st.warning('Verifique que todos los valores de las métricas hayan sido ingresados')
            st.session_state.countSubmitted += 1
        else:
            with st.spinner("Procesando..."):
                t.sleep(1)
                try:
                    result_df = self.evaluator.predict(metricas_modelo)
                    st.success("✅ ¡Hecho!")
                    st.write(f'El dataset {Nombre} tiene un incentivo de uso de {result_df}')   
                except Exception as ex:
                    st.error("Algo salió mal", icon="🚨")
    
    def render_csv_form(self):
        st.subheader("Cargar CSV con las calificaciones de calidad")
        csv_file = st.file_uploader("Sube un archivo CSV", type=["csv"])
        if csv_file:
            df = pd.read_csv(csv_file, sep=';')
            print(df)
            st.write("Vista previa del DataFrame:")
            st.write(df.head())
            result_df = self.evaluator.predict(df)
            st.success("✅ ¡Hecho!")
            st.write(f'El dataset tiene un incentivo de uso de {result_df}')   

if __name__ == "__main__":
    app = StreamlitApp()
    app.run()
