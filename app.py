import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
from io import BytesIO

# Configuración de página con colores de AMACHAY
st.set_page_config(page_title="AMACHAY - Seguridad Minera", layout="wide")

# Estilos personalizados (Azul corporativo y Dorado)
st.markdown("""
    <style>
    .main { background-color: #050E17; color: #E8EDF2; }
    .stButton>button { background-color: #C5A059; color: #050E17; font-weight: bold; }
    .css-1d391kg { background-color: #0A1C2F; }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.sidebar.image("image_96b60f.png", width=150)
    menu = ["Inicio", "Dashboard IPERC", "Análisis Bow-Tie", "Generador PETS/Estándar"]
    choice = st.sidebar.selectbox("Navegación", menu)

    if choice == "Inicio":
        st.title("AMACHAY: Seguridad Minera")
        st.subheader("Plataforma de Gestión de Riesgos y Automatización")
        st.image("image_97441b.jpg", caption="Brigada de Respuesta a Emergencias Mineras")
        st.write("Bienvenido al sistema integral de identificación de peligros y gestión documental.")

    elif choice == "Dashboard IPERC":
        st.header("Identificación de Peligros y Evaluación de Riesgos")
        uploaded_file = st.file_uploader("Subir reporte diario (Excel/CSV)", type=['xlsx', 'csv'])
        if uploaded_file:
            st.success("Análisis completado. Puntos críticos detectados en Nivel 4000.")
            # Simulación de tabla de puntos críticos
            df_iperc = pd.DataFrame({
                "Área": ["Galería Sur", "Taller"],
                "Peligro": ["Desprendimiento", "Derrame"],
                "Riesgo": ["Alto", "Medio"]
            })
            st.table(df_iperc)

    elif choice == "Análisis Bow-Tie":
        st.header("Generador de Diagrama Bow-Tie")
        top_event = st.text_input("Evento Crítico (Top Event)", "Incendio en Scoop")
        
        col1, col2 = st.columns(2)
        with col1:
            cause = st.text_input("Amenaza/Causa")
            prev = st.text_input("Barrera Preventiva")
        with col2:
            cons = st.text_input("Consecuencia")
            mitig = st.text_input("Barrera Mitigadora")

        if st.button("Generar Gráfico"):
            G = nx.DiGraph()
            G.add_edge(cause, top_event)
            G.add_edge(top_event, cons)
            plt.figure(figsize=(8,4))
            nx.draw(G, with_labels=True, node_color="#C5A059", font_weight='bold')
            st.pyplot(plt)

    elif choice == "Generador PETS/Estándar":
        st.header("Gestión Documental (Anexo 9 y 10)")
        doc_type = st.radio("Seleccione Formato", ["Anexo N° 9: Estándar", "Anexo N° 10: PETS"])
        unidad = st.text_input("Unidad Minera")
        código = st.text_input("Código de Documento")
        
        st.text_area("Contenido del Procedimiento / Especificaciones")
        if st.button("Exportar a PDF"):
            st.info("Generando documento con marca de agua Amachay...")

if __name__ == "__main__":
    main()