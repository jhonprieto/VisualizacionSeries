import streamlit as st
import pandas as pd

# ── Configuración de página ──────────────────────
st.set_page_config(
    page_title="Mi App de Ventas",
    page_icon="📊",
    layout="wide"
)

# ── Sidebar ──────────────────────────────────────
with st.sidebar:
    st.header("Filtros")
    año = st.selectbox("Año", [2023, 2024, 2025])
    mostrar_tabla = st.checkbox("Mostrar tabla", value=True)

# ── Título ───────────────────────────────────────
st.title(f"Reporte de Ventas {año}")
st.markdown("Resumen mensual de ventas del año seleccionado.")

# ── Métricas en columnas ─────────────────────────
col1, col2, col3 = st.columns(3)
col1.metric("Total ventas", "$2,850", "+12%")
col2.metric("Clientes", "340", "+5")
col3.metric("Promedio/mes", "$237", "-3%")

# ── Datos y gráfico ──────────────────────────────
ventas = [120, 130, 150, 170, 200, 250,
           300, 350, 400, 450, 380, 320]
meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun",
          "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]

df = pd.DataFrame({"Mes": meses, "Ventas": ventas})
df = df.set_index("Mes")

st.subheader("Ventas mensuales")
st.line_chart(df)

# ── Tabla condicional ────────────────────────────
if mostrar_tabla:
    st.subheader("Detalle")
    st.dataframe(df, use_container_width=True)

# ── Sección expandible ───────────────────────────
with st.expander("¿Cómo se calcularon estos datos?"):
    st.write("Los datos son ficticios, ideales para practicar.")

# ── Mensajes de estado ───────────────────────────
st.success("¡App cargada correctamente!")
