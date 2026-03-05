import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Control de Asesores - Taller", layout="wide")

st.title("🚗 Gestión de Asesores: Chapa y Pintura")

# 1. SIMULACIÓN DE DATOS (Sustituye esto luego con tu Google Sheet)
data = {
    "Asesor": ["Juan Pérez", "María García", "Carlos Rodríguez", "Ana Martínez"],
    "Vehículos en Proceso": [5, 3, 8, 4],
    "Estado": ["Activo", "En Pausa", "Activo", "Almuerzo"],
    "Última Actualización": ["10:00 AM", "09:45 AM", "10:15 AM", "08:30 AM"]
}
df = pd.DataFrame(data)

# 2. BARRA LATERAL (Filtros)
st.sidebar.header("Filtros de Búsqueda")
asesor_sel = st.sidebar.multiselect(
    "Selecciona el Asesor:",
    options=df["Asesor"].unique(),
    default=df["Asesor"].unique()
)

df_filtrado = df[df["Asesor"].isin(asesor_sel)]

# 3. INDICADORES RÁPIDOS (Métricas)
col1, col2, col3 = st.columns(3)
col1.metric("Total Vehículos", df_filtrado["Vehículos en Proceso"].sum())
col2.metric("Asesores Activos", len(df_filtrado[df_filtrado["Estado"] == "Activo"]))
col3.metric("Promedio por Asesor", df_filtrado["Vehículos en Proceso"].mean())

st.divider()

# 4. TABLA DE CONTROL
st.subheader("Estado actual del taller")
st.dataframe(df_filtrado, use_container_width=True)

# 5. FORMULARIO PARA AGREGAR NOTAS (Ejemplo de interactividad)
with st.expander("Añadir reporte de incidencia"):
    with st.form("mi_formulario"):
        asesor_incidencia = st.selectbox("Asesor", df["Asesor"])
        detalle = st.text_area("Detalle de la novedad")
        enviado = st.form_submit_button("Guardar Reporte")
        if enviado:
            st.success(f"Reporte guardado para {asesor_incidencia}")
