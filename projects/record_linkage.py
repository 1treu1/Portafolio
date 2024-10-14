import streamlit as st

def display_record_linkage():
    st.write("## Overview - RecordLinkage")
    st.image("https://recordlinkage.readthedocs.io/en/latest/_images/indexing_basic.png", caption="Record Linkage Project", use_column_width=True)
    st.write("""
        **Problema**: En Mercado Libre, es necesario deduplicar una base de datos para mantener registros únicos de clientes.

        **Solución**: Se utilizó la biblioteca RecordLinkage para entrenar un modelo NLP y agrupar los registros duplicados.

        **Pasos del Proyecto**:
        - Creación de una base de datos de ejemplo con Faker.
        - Limpieza de datos: conversión a minúsculas, eliminación de caracteres especiales.
        - Uso de la distancia Jaro-Winkler para identificar registros duplicados.

        **Librerías Utilizadas**: pandas, recordlinkage, faker.
        
        [Ver en GitHub](https://github.com/1treu1/Deduplicacion-de-Datos/blob/main/RecordLinKage/Data_Deduplication_with_RecordLinKage.ipynb)

    """)

