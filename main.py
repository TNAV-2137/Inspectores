import streamlit as st
import streamlit.components.v1 as components
import os
import base64

# Configuración de la página
st.set_page_config(layout="wide", page_title="Mapa Inspectores PNA")

# Función para convertir imagen local a base64 (necesario para HTML en Streamlit)
def get_image_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# --- INICIO DE LA SECCIÓN DE ENCABEZADO CENTRADO ---

path_escudo = "escudo_dtnav.png"

if os.path.exists(path_escudo):
    # Convertimos la imagen para que el HTML la reconozca correctamente
    img_base64 = get_image_base64(path_escudo)
    
    st.markdown(
        f"""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; margin-bottom: 20px;">
            <img src="data:image/png;base64,{img_base64}" width="250" style="margin-bottom: 10px;">
            <h1 style="margin-top: 0px;">Departamento Técnico de la Navegación - Distribución de Inspectores</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
else:
    # Si no existe la imagen, centramos solo el título
    st.markdown("<h1 style='text-align: center;'>Departamento Técnico de la Navegación - Distribución de Inspectores</h1>", unsafe_allow_html=True)
    st.warning("No se encontró el archivo 'escudo_dtnav.png'. Asegúrate de subirlo a la carpeta raíz de GitHub.")

# --- FIN DE LA SECCIÓN DE ENCABEZADO ---

# 3. Cargar el mapa
with st.spinner("Cargando el mapa de inspectores..."):
    path_mapa = "Mapa_Inspectores_Actualizado.html"
    if os.path.exists(path_mapa):
        with open(path_mapa, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Ajuste de ancho automático para que el mapa ocupe toda la pantalla
        components.html(html_content, height=800, scrolling=True)
    else:
        st.error(f"No se encontró el archivo del mapa ('{path_mapa}') en GitHub.")
