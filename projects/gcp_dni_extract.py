import streamlit as st
import requests
import pandas as pd

def display_gcp_dni_extract():
    st.write("## Overview - GCP DNI Extract")
    st.image("https://miro.medium.com/v2/resize:fit:875/1*P61GW6qXJOjqLPN98uS56Q.gif", caption="GCP DNI Extract Project", use_column_width=True)
    st.write("""
        **Problema**: Es necesario automatizar el proceso de extracción de información de documentos de identidad para mejorar la eficiencia del negocio.

        **Solución**: Utilizar el servicio Document AI de Google Cloud Platform para extraer la información de los DNI, empleando una solución basada en la nube que proporciona OCR avanzado.

        **Pasos del Proyecto**:
        - **Carga de Documentos**: Los documentos de identidad se suben al sistema.
        - **Extracción Automatizada**: Uso de Google Document AI para reconocer y extraer la información relevante de manera precisa y eficiente.

        **Librerías Utilizadas**: `requests`, `pandas`.

        [Probar](https://github.com/1treu1/GCP-DNI-Extract)
    """)

    # Cargar un archivo de imagen o PDF
    uploaded_file = st.file_uploader("Sube tu imagen o PDF del DNI:", type=["jpg", "jpeg", "png", "pdf"])

    if uploaded_file is not None:
        # Realizar la llamada a la API
        url = "https://rock-dragon-403212.ue.r.appspot.com/files/"
        files = {"file": uploaded_file}

        try:
            response = requests.post(url, files=files)
            response.raise_for_status()  # Verifica si la solicitud fue exitosa
            result = response.json()

            # Mostrar el resultado del OCR en una tabla
            if isinstance(result, dict):
                df = pd.DataFrame([result['document_result']])
                st.write("### Resultados del OCR en Tabla:")
                st.table(df)
            else:
                st.write("Formato de respuesta inesperado")
                st.json(result)

        except requests.exceptions.RequestException as e:
            st.error(f"Error en la solicitud a la API: {e}")
