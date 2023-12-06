import pandas as pd
import plotly.express as px
import streamlit as st
        
car_data = pd.read_csv('vehicles_us.csv') # leer los datos

#Encabezado
st.header('Venta de autos')
hist_button = st.button('Construir histograma') # crear un botón
        
if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
            
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)



#prueba casilla de verificación

# Crear casillas de verificación para elegir la columna
option_odometer = st.checkbox('Coches por tipo')
option_price = st.checkbox('Precio por modelo')

# Mostrar el gráfico correspondiente a la elección del usuario
if option_odometer:
    st.write('Creación de un gráfico de barras para el número de coches por tipo de transmisión')
    fig = px.bar(car_data, x="odometer", y='transmission')
    st.plotly_chart(fig, use_container_width=True)

if option_price:
    st.write('Creación de un gráfico de dispersión para los precios por modelo')
    fig = px.scatter(car_data, x="price", y="model")
    st.plotly_chart(fig, use_container_width=True)
