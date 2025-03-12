import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
    np.random.randn(20, 3), #generar valores aleatorios
    columns = ['a','b','c'] #Generar las columnas
)
st.write(chart_data) #mostrar en tabla o interfaz de web. Con print resultados en la consola
st.line_chart(chart_data) #Crear lineas interactivas