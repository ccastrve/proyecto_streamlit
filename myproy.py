import streamlit as st
from datetime import date, datetime, time
import pandas as pd
import numpy as np


st.title('Mi primer proyecto Streamlit CCV')

# usando nomenclatuta markdown
st.write('Hola **Cristhian Castro**, como estás?')
st.write('# Mi subtitulo Nivel 1')
st.write('## Mi subtitulo Nivel 2')
st.write('### Mi subtitulo Nivel 3')
st.write('#### Mi subtitulo Nivel 4')

# para ejecutar --> streamlit run <nombre_archivo>
# los elementos de entrada se declaran como variables

# SLIDER
num = st.slider('Elegir nivel', 0, 100, step = 1)
st.write('El número ingresado es {}'.format(num))

# Slider de horas
horario = st.slider("Asesorías", value = (time(11,30), time(12,45)))
st.write("Agendado para las : {}".format(horario))

# Slider de fechas
fecha = st.slider("Casos ocurridos", value=datetime(2020,1,1,9,30),
        format='DD/MM/YY - hh:mm')
st.write('Fecha seleccionada: {}'.format(fecha))

# ingreso de fechas con calendario
cumple = st.date_input('Fecha de cumpleaños', 
        date(2019,7,6))
st.write('Tu cumpleaños es: {}'.format(cumple))

# un Select box
option = st.selectbox('¿Cómo desea ser contactado?',
        ('Email', 'Teléfono', 'Whatsapp'))
st.write('Seleccionó: {}'.format(option))

# Lista de selección - gráfico
# randn(n) genera valores aleatorios según distribución normal estándar
n = st.slider('número', 5, 100, step = 1)
chart_data = pd.DataFrame(np.random.randn(n), columns=['data'])
st.line_chart(chart_data)

# creando mapa
# randn(1000,2) genera mil tuplas de 2 elementos
df = pd.DataFrame(
    np.random.randn(1000, 2)/[50,50] + [37.76,-122.4],
    columns=['lat', 'lon'])

















