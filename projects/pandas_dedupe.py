import streamlit as st

def display_pandas_dedupe():
    st.write("## Overview - Pandas Dedupe")
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRRaJ10QzX3jvXcKYwaIQAB1zH6Y7TRqVjipg&usqp=CAU", caption="Pandas Dedupe Project", use_column_width=True)
    st.write("""
        **Problema**: En Mercado Libre, existe una base de datos con registros duplicados de clientes debido a malas prácticas. La calidad de los datos se ve comprometida y se requiere identificar duplicados.

        **Solución**: Se utilizó la biblioteca Pandas Dedupe para entrenar un modelo de NLP que pueda identificar y agrupar los registros duplicados.

        **Pasos del Proyecto**:
        - Instalación de las librerías necesarias.
        - Creación de una base de datos de ejemplo con Faker.
        - Introducción de duplicados en los datos.
        - Entrenamiento del modelo para identificar duplicados.

        **Librerías Utilizadas**: pandas, dedupe, faker.
        
        [Ver en GitHub](https://github.com/1treu1/Deduplicacion-de-Datos/blob/main/Pandas%20Dedupe/Data_Deduplication_with_Dedupe_Pandas.ipynb)

    """)

