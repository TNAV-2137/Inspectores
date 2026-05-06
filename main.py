import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")
st.title("Análisis de Dependencias - PNA")

# Cambia "tu_archivo.html" por el nombre real:
with open("Mapa_Inspectores_Actualizado.html", 'r', encoding='utf-8') as f:
    html_data = f.read()

components.html(html_data, height=800)
