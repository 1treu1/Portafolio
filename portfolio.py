import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
from projects.pandas_dedupe import display_pandas_dedupe
from projects.record_linkage import display_record_linkage
from projects.the_fuzz import display_the_fuzz
from projects.dni_extract import display_dni_extract
from projects.gcp_dni_extract import display_gcp_dni_extract
from projects.video_games_portfolio import display_video_games_portfolio


# Configuración de la página
st.set_page_config(page_title="Luis Medina - Data Science Portfolio", page_icon="https://cdn-icons-png.flaticon.com/512/3013/3013760.png", layout="wide")

# Colores base
def set_base_styles():
    st.markdown("""
        <style>
            body {
                background-color: #ffffff;
                color: #333333;
            }
            .main-header {
                background-color: #f0f2f6ff;
                color: #808080ff;
                padding: 20px;
                text-align: center;
            }
            .project-card {
                border: 2px solid #ffe600;
                border-radius: 10px;
                padding: 15px;
                margin-bottom: 20px;
                background-color: #f9f9f9;
            }
            .btn-link {
                background-color: #ffe600;
                color: #000000;
                text-decoration: none;
                padding: 8px 15px;
                border-radius: 5px;
            }
            .btn-link:hover {
                background-color: #000000;
                color: #FFD700;
            }
        </style>
        """, unsafe_allow_html=True)

set_base_styles()

# Barra lateral de navegación con streamlit-option-menu
# Encabezado
def display_header():
    st.markdown('<div class="main-header"><h1>Luis Medina - Data Science Portfolio</h1><p>Bienvenido a mi portafolio, explora mis proyectos en ciencia de datos</p></div>', unsafe_allow_html=True)

display_header()

with st.sidebar:
    section = option_menu(
        "Navegación",
        ["Acerca de mí", "Proyectos", "Contacto"],
        icons=["house", "bar-chart", "envelope"],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {"padding": "5px", "background-color": "#ededed"},
            "icon": {"color": "black", "font-size": "25px"},
            "nav-link": {"font-size": "16px", "text-align": "left", "margin": "0px", "--hover-color": "#eee", "font-weight": "bold", "color": "black"},
            "nav-link-selected": {"background-color": "#FFD700"},
        },
    )

# Sub-sección de Proyectos
if section == "Proyectos":
    project = st.selectbox("Selecciona un proyecto:", [
        "GCP DNI Extract",
        "DNI Extract", 
        "Pandas Dedupe", 
        "RecordLinkage", 
        "TheFuzz",
        "Video Games Portfolio"
    ])

    # Llamar a la función correspondiente de cada proyecto o su overview
    if project == "Pandas Dedupe":
        display_pandas_dedupe()
    elif project == "RecordLinkage":
        display_record_linkage()
    elif project == "TheFuzz":
        display_the_fuzz()
    elif project == "DNI Extract":
        display_dni_extract()
    elif project == "GCP DNI Extract":
        display_gcp_dni_extract()
    elif project == "Video Games Portfolio":
        display_video_games_portfolio()

# Sección "Acerca de mí"
def display_about():
    st.write("## Acerca de mí")
    st.write("""
        Soy Luis Medina, un científico de datos apasionado por analizar y resolver problemas complejos utilizando datos.
        Tengo experiencia en Python, machine learning, análisis de datos, y tecnologías relacionadas. En este portafolio podrás encontrar
        algunos de los proyectos en los que he trabajado y que muestran mis habilidades y capacidades técnicas.
    """)

# Sección "Contacto"
def display_contact():
    st.write("## Contacto")
    st.write("Si deseas ponerte en contacto conmigo, puedes enviarme un mensaje a través de mi [LinkedIn](https://www.linkedin.com/in/luis-medina-533370192).")

# Mostrar secciones según la navegación seleccionada
if section == "Acerca de mí":
    display_about()
elif section == "Contacto":
    display_contact()