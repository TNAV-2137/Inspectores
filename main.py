import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="Mapa PNA")

st.title("Análisis de Dependencias - Prefectura Naval Argentina")

try:
    with open("Mapa_Inspectores_Actualizado.html", 'r', encoding='utf-8') as f:
        html_data = f.read()
    components.html(html_data, height=800, scrolling=True)
except FileNotFoundError:
    st.error("No se encontró el archivo del mapa.")
