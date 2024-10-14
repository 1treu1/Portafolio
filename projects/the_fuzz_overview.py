import streamlit as st

def display_the_fuzz_overview():
    st.write("## Overview - The Fuzz")
    st.image("https://m.media-amazon.com/images/M/MV5BNDRkYjI4NmMtNmQ4Yy00NWFhLWFlYWUtYWJlZWIyN2U2MjlmXkEyXkFqcGdeQXVyNjgzNDU2ODI@._V1_.jpg", caption="The Fuzz Project", use_column_width=True)
    st.write("""
        **Problema**: La base de datos de clientes de Mercado Libre contiene registros duplicados que afectan la calidad de los datos.

        **Solución**: Se utilizó TheFuzz para aplicar técnicas de comparación difusa para encontrar similitudes entre registros.

        **Pasos del Proyecto**:
        - Creación de una base de datos de ejemplo.
        - Introducción de registros duplicados.
        - Uso de algoritmos de similitud (Jaro-Winkler, Levenshtein) para determinar duplicados.

        **Librerías Utilizadas**: pandas, thefuzz, faker.
        
        [Ver en GitHub](https://github.com/1treu1/Deduplicacion-de-Datos/blob/main/TheFuzz/Data_Deduplication_with_TheFuzz.ipynb)


    """)

