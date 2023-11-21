# Python In-built packages
from pathlib import Path
import PIL

# External packages
import streamlit as st

# Local Modules
import settings
import helper

# Setting page layout
st.set_page_config(
    page_title="Deteccion de Plagas en la agricultura Mexicana",
    # page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Encabezado 
st.title("Deteccion de Plagas en la agricultura Mexicana")

# Barra lateral 
st.sidebar.header("Configuración del modelo de aprendizaje automático")

# Opciones de Modelo
model_type = st.sidebar.radio(
    "Seleccionar tarea", ['Deteccion' ])

confidence = float(st.sidebar.slider(
    "Seleccione la confianza del modelo", 25, 100, 40)) / 100

# Selecting Detection Or Segmentation
#if model_type == 'Deteccion':
#  model_path = Path(settings.DETECTION_MODEL)
#elif model_type == 'Segmentation':
#    model_path = Path(settings.SEGMENTATION_MODEL)

# Load Pre-trained ML Model
#try:
#    model = helper.load_model(model_path)
# except Exception as ex:
#    st.error(f"Unable to load model. Check the specified path: {model_path}")
#    st.error(ex)

st.sidebar.header("Imagen/Config")
source_radio = st.sidebar.radio(
    "Seleccione Fuente", settings.SOURCES_LIST)

source_img = None
# If image is selected
if source_radio == settings.IMAGE:
    source_img = st.sidebar.file_uploader(
        "Elige una imagen...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))
 

