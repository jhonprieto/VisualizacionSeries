import streamlit as st
import pandas as pd

ventas = {
    "Ene": 120, "Feb": 130, "Mar": 150, "Abr": 170,
    "May": 200, "Jun": 250, "Jul": 300, "Ago": 350,
    "Sep": 400, "Oct": 450, "Nov": 380, "Dic": 320
}

# Widget de filtro
periodo = st.radio(
    "Mostrar periodo",
    ["Primer semestre", "Segundo semestre", "Todo el año"],
    horizontal=True
)

# Filtrar según selección
meses_todos = list(ventas.keys())
if periodo == "Primer semestre":
    meses = meses_todos[:6]
elif periodo == "Segundo semestre":
    meses = meses_todos[6:]
else:
    meses = meses_todos

df = pd.DataFrame({"Ventas": [ventas[m] for m in meses]}, index=meses)
st.line_chart(df)