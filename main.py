import streamlit as st
import streamlit.components.v1 as components
import os

# Configuración de la página
st.set_page_config(layout="wide", page_title="Mapa Inspectores PNA")

# --- DISEÑO INSTITUCIONAL CON CENTRADO ABSOLUTO ---

# Definimos el nombre del archivo
archivo_escudo = "escudo_dtnav.png"

if os.path.exists(archivo_escudo):
    # Usamos HTML para centrar y definir un tamaño fijo (250px en este caso)
    # También añadimos un margen inferior para separarlo del título
    st.markdown(
        f"""
        <div style="display: flex; justify-content: center;">
            <img src="https://raw.githubusercontent.com/TNAV-2137/Inspectores/main/{archivo_escudo}" width="250">
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    st.warning(f"No se encontró {archivo_escudo} en el repositorio.")

# Título centrado debajo del escudo
st.markdown(
    "<h1 style='text-align: center; margin-top: 0;'>Departamento Técnico de la Navegación - Inspectores</h1>", 
    unsafe_allow_html=True
)

# --- CARGA DEL MAPA ---
path_mapa = "Mapa_Inspectores_Actualizado.html"

if os.path.exists(path_mapa):
    with open(path_mapa, 'r', encoding='utf-8') as f:
        html_content = f.read()
    # Mostramos el mapa
    components.html(html_content, height=750, scrolling=True)
else:
    st.error("No se encontró el archivo del mapa en GitHub.")
