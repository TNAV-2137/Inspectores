import streamlit as st
import streamlit.components.v1 as components
import os

# Configuración de la página
st.set_page_config(layout="wide", page_title="Mapa Inspectores PNA")

# --- DISEÑO INSTITUCIONAL CENTRADO ---

# Usamos contenedores para asegurar el centrado
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # 1. Mostrar el Escudo Centrado
    if os.path.exists("escudo_dtnav.png"):
        # st.image centrará la imagen automáticamente dentro de la columna
        st.image("escudo_dtnav.png", width=200) 
    else:
        st.warning("No se encontró 'escudo_dtnav.png' en GitHub.")

    # 2. Título con estilo CSS para asegurar el centrado del texto
    st.markdown(
        "<h1 style='text-align: center;'>Departamento Técnico de la Navegación - Distribución de Inspectores</h1>", 
        unsafe_allow_html=True
    )

# --- CARGA DEL MAPA ---
path_mapa = "Mapa_Inspectores_Actualizado.html"

if os.path.exists(path_mapa):
    with open(path_mapa, 'r', encoding='utf-8') as f:
        html_content = f.read()
    # Mostramos el mapa ocupando el ancho completo de la página
    components.html(html_content, height=750, scrolling=True)
else:
    st.error(f"No se encontró el archivo del mapa ('{path_mapa}') en GitHub.")
