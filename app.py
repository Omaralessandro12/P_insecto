

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

st.sidebar.header("Imagen/Config")
source_radio = st.sidebar.radio(
    "Seleccione Fuente", settings.SOURCES_LIST)



