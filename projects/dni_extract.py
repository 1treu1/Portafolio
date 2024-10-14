import streamlit as st

def display_dni_extract():
    st.write("## Overview - DNI Extract")
    st.image("https://nanonets.com/blog/content/images/2020/09/landing-ocr-1.gif", caption="DNI Extract Project", use_column_width=True)
    st.write("""
        **Problema**: En Mercado Libre, se requiere extraer la información relevante de documentos de identidad para automatizar el proceso de validación.

        **Solución**: Se desarrolló un proyecto para extraer información a partir de los DNI utilizando técnicas de Detección de Objetos y Reconocimiento Óptico de Caracteres (OCR).

        **Pasos del Proyecto**:
        - **Detección de Objetos**: Entrenamiento de un modelo de detección con YOLOv8 para identificar las áreas relevantes en el DNI.
        - **OCR en los Bounding Boxes**: Uso de EasyOCR para extraer el texto dentro de las áreas detectadas.

        **Librerías Utilizadas**: `ultralytics`, `yolov8`, `easyocr`, `cv2`, `numpy`.

        [Ver en GitHub](https://github.com/1treu1/DNI-Extract)
    """)

