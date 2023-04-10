#importacion librerias
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#Cofiguracion pagina
st.set_page_config(
    page_title="Dashboard",
    page_icon="🎶",
    layout="wide",
    initial_sidebar_state="expanded"
)

with st.sidebar:
    #Titulo inicial
    st.title("Bienvenidos a mi primer Dashboard")
    #texto
    st.write("(Taylor's Version)")
    # descripcion
    st.markdown('Dashboard para analizar las musica que se encuentra en Spotify de la poderosa Taylor Swift.')
    # link dataset
    st.markdown('Dataset: [Taylor Swift Spotify](https://www.kaggle.com/datasets/jarredpriester/taylor-swift-spotify-dataset)')
    # link github
    st.markdown('Github: [KitzelZ/Ciencia-de-Datos](https://github.com/KitzelZ/Ciencia-de-Datos)')
    st.markdown('Twitter: [@thekarnotaurus](https://twitter.com/thekarnotaurus)')


#carga de datos
tay_data = pd.read_csv('taylor_swift_spotify.csv')
#quitar valres nulos
tay_data = tay_data.drop(columns=['Unnamed: 0'])

#ms a min
tay_data['duration_s'] = tay_data['duration_ms']/1000
tay_data['duration_m'] = tay_data['duration_s']/60

#cambio de tipode dato
tay_data['release_date'] = pd.to_datetime(tay_data['release_date'])
tay_data['name']=tay_data['name'].astype('string')
tay_data['album']=tay_data['album'].astype('string')

#quitar valores
tay_data = tay_data.drop(columns=['duration_ms','duration_s'])

#mostrar momentaneamente los datos
#st.write(tay_data)

#Conatinner principal
with st.container():
    #titulo
    st.title('Taylor Swift Spotify')


#Conatinner top------------------------------
with st.container():
    #titulo
    st.markdown('## Top 10 Spotify')

#Canciones Top
top_data = tay_data.sort_values('popularity', ascending = False)[['name', 'album', 'release_date', 'track_number', 'acousticness', 'danceability', 'energy', 'instrumentalness',
       'liveness', 'loudness', 'speechiness', 'tempo', 'valence', 'popularity',
       'duration_m']].head(10)
top_data.index = np.arange(1, len(top_data)+1)
#st.table(top_data)

#grafico de barras 
st.bar_chart(top_data, 
             y='popularity', 
             x='name')

#Top 20 Canciones 

#chart_url = "https://datawrapper.dwcdn.net/lM4t4/2/"
#st.title("Top 20")
#st.markdown(f'<iframe src="{chart_url}" frameborder="0" scrolling="no" width="100%" height="800"></iframe>', unsafe_allow_html=True)

#Top Unpopular Song
chart_url = "https://datawrapper.dwcdn.net/Z1wh8/1/"
st.title("Top Unpopular Song")
st.markdown(f'<iframe src="{chart_url}" frameborder="0" scrolling="no" width="100%" height="800"></iframe>', unsafe_allow_html=True)

#Top Unpopular Song
chart_url = "https://datawrapper.dwcdn.net/L166D/1/"
st.title("Variables Spotify")
st.markdown(f'<iframe src="{chart_url}" frameborder="0" scrolling="no" width="100%" height="800"></iframe>', unsafe_allow_html=True)