import streamlit as st

def display_video_games_portfolio():
    st.write("## Overview - Video Games Portfolio")
    st.image("https://1treu1.github.io/images/01.gif", caption="Video Games Portfolio", use_column_width=True)
    st.write("""
        **Problema**: Mostrar el desarrollo de habilidades y proyectos realizados en el área de videojuegos.

        **Solución**: Se presenta un portafolio de videojuegos desarrollados utilizando Unity 3D. Cada uno de estos proyectos incluye diferentes mecánicas y dinámicas de juego implementadas con C#.

        **Pasos del Proyecto**:
        - **Desarrollo con Unity**: Creación de juegos en Unity 3D, incorporando diferentes dinámicas y experiencias interactivas.
        - **Programación en C#**: Implementación de lógica de juego utilizando C# para el manejo de eventos y mecánicas de juego.

        **Librerías Utilizadas**: `Unity`, `C#`.

        [Ver en GitHub](https://1treu1.github.io/)
    """)

