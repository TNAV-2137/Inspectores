import streamlit as st
import streamlit.components.v1 as components
import os
import base64

# 1. Configuración de la página
st.set_page_config(layout="wide", page_title="Mapa Inspectores PNA")

# 2. Función para cargar la imagen de fondo y convertirla a Base64
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def set_png_as_page_bg(bin_file):
    bin_str = get_base64_of_bin_file(bin_file)
    page_bg_img = f'''
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    
    /* Estilo para que el título sea legible sobre la imagen */
    h1 {{
        color: white !important;
        text-shadow: 2px 2px 4px #000000;
        background-color: rgba(0, 0, 50, 0.5); /* Fondo semitransparente azul oscuro */
        padding: 10px;
        border-radius: 10px;
    }}

    /* Contenedor del mapa: le damos un fondo sólido para que no se transparente el barco */
    iframe {{
        background-color: white;
        border-radius: 10px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.5);
    }}
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)

# Aplicar el fondo si el archivo existe
if os.path.exists("fondo.png"):
    set_png_as_page_bg("fondo.png")

# --- DISEÑO INSTITUCIONAL ---

# 1. Escudo Centrado
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
with col3:
    if os.path.exists("escudo_dtnav.png"):
        st.image("escudo_dtnav.png", width=450)
    else:
        st.error("No se encontró 'escudo_dtnav.png'")

# 2. Título Centrado
st.markdown(
    "<h1 style='text-align: center; margin-top: -20px;'>Departamento Técnico de la Navegación - Inspectores</h1>", 
    unsafe_allow_html=True
)

# --- CARGA DEL MAPA ---
path_mapa = "Mapa_Inspectores_Actualizado.html"

if os.path.exists(path_mapa):
    with open(path_mapa, 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # El mapa se verá sobre un fondo blanco sólido para no superponerse visualmente con la foto
    components.html(html_content, height=750, scrolling=True)
else:
    st.error("No se encontró el archivo del mapa en GitHub")
