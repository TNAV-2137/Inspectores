import streamlit as st
import streamlit.components.v1 as components
import os

# Configuración de la página
st.set_page_config(layout="wide", page_title="Mapa Inspectores PNA")

# --- DISEÑO INSTITUCIONAL ---

# 1. Escudo Centrado usando columnas (Método más estable)
col1, col2, col3 = st.columns([1, 1, 1]) # Tres columnas iguales

with col2:
    if os.path.exists("escudo_dtnav.png"):
        # Ajustamos el ancho a 250 para que se vea igual a tu captura previa
        st.image("escudo_dtnav.png", width=400)
    else:
        st.error("No se encontró el archivo 'escudo_dtnav.png' en el repositorio.")

# 2. Título Centrado
st.markdown(
    "<h1 style='text-align: center; margin-top: -20px;'>Departamento Técnico de la Navegación - Distribucion de Inspectores</h1>", 
    unsafe_allow_html=True
)

# --- ESPACIADOR ---
st.markdown("<br>", unsafe_allow_html=True)

# --- CARGA DEL MAPA ---
path_mapa = "Mapa_Inspectores_Actualizado.html"

if os.path.exists(path_mapa):
    with open(path_mapa, 'r', encoding='utf-8') as f:
        html_content = f.read()
    # Mostramos el mapa ocupando el ancho completo
    components.html(html_content, height=750, scrolling=True)
else:
    st.error(f"Archivo de mapa no encontrado.")
