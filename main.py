import streamlit as st
import streamlit.components.v1 as components
import os

# Configuración de la página (esto es opcional pero recomendado)
st.set_page_config(layout="wide", page_title="Mapa Inspectores PNA")

# --- AQUÍ ESTÁ EL CAMBIO ---

# 1. Mostrar el Escudo
# Usamos 'use_column_width=False' y 'width=150' para que no ocupe todo el ancho
# y se vea como un logo arriba del título.
# Asegúrate de que el archivo 'escudo_dtnav.png' esté en tu GitHub.

# Si quieres centrar la imagen y el título, puedes usar columnas:
col1, col2, col3 = st.columns([1,2,1]) # Creamos 3 columnas, la del medio más ancha

with col2: # Todo lo que pongamos aquí estará centrado
    if os.path.exists("escudo_dtnav.png"):
        st.image("escudo_dtnav.png", width=120) # Ajusta el 'width' (ancho) a tu gusto
    else:
        st.warning("No se encontró el archivo del escudo ('escudo_dtnav.png') en GitHub.")

    # 2. Mostrar el Título (debajo del escudo)
    st.title('Departamento Técnico de la Navegación - Distribucion de Inspectores')

# --- FIN DEL CAMBIO ---

# 3. Cargar el mapa (esto ya lo tienes funcionando)
with st.spinner("Cargando el mapa de inspectores..."):
    # Tu código actual para cargar el mapa:
    path_mapa = "Mapa_Inspectores_Actualizado.html"
    if os.path.exists(path_mapa):
        with open(path_mapa, 'r', encoding='utf-8') as f:
            html_content = f.read()
        components.html(html_content, height=700, scrolling=True)
    else:
        st.error(f"No se encontró el archivo del mapa ('{path_mapa}') en GitHub.")
