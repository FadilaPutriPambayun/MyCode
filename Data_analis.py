import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import altair as alt
import plotly.express as px
import pandas as pd
import scipy as sp
import seaborn as sns

#konfigurasi halaman
st.set_page_config(
    page_title = "Bike Sharing Dashboard",
    page_icon = "🚵🏼‍♀️",
    layout = "wide",
    initial_sidebar_state = "expanded"
)
alt.themes.enable("default")

#memuat data
df_reshaped = pd.read_csv('C:\\Users\\HP\\OneDrive - mail.unnes.ac.id\\BANGKIT\\PROYEK\\Data Analisis\\day.csv')

season_dict = {1: 'Winter', 2: 'Spring', 3: 'Summer', 4: 'Fall'}
df_reshaped['season_label'] = df_reshaped['season'].map(season_dict)

#menambahkan sidebar
with st.sidebar:
    st.title('🚵🏼‍♀️ Bike Sharing Dashboard')

    #dropdown untuk memilih analisis
    analysis_option = st.selectbox(
        'Select Analysis',
        ['Pengaruh Musim Terhadap Penyewaan', 'Pengaruh Cuaca Terhadap Penyewaan']
    )

#analisis pengaruh musim terhadap penyewaan
if analysis_option == 'Pengaruh Musim Terhadap Penyewaan':
    st.header("Pengaruh Musim Terhadap Penyewaan Sepeda Harian")

    #rata-rata penyewaan sepeda per musim
    season_avg = df_reshaped.groupby('season_label')['cnt'].mean().sort_values()

    #plot rata-rata penyewaan sepeda per musim
    fig, ax = plt.subplots()
    season_avg.plot(kind='bar', color='skyblue', ax=ax)
    ax.set_title('Avarage Daily Bike Rentals per Season')
    ax.set_xlabel('Season')
    ax.set_ylabel('Avarage Rentals')
    st.pyplot(fig)

#analisis pengaruh cuaca terhadap penyewaan
elif analysis_option == 'Pengaruh Cuaca Terhadap Penyewaan':
    st.header("Pengaruh Cuaca Terhadap Penyewaan Sepeda Harian")

    #scatter plot antara suhu, kelembaban, dan kecepatan angin dengan penyewaan
    fig, axs = plt.subplots(1, 3, figsize=(18, 5))
    sns.scatterplot(x='temp', y='cnt', data=df_reshaped, ax=axs[0], color='orange').set(title='Temperature vs Rentals')
    sns.scatterplot(x='hum', y='cnt', data=df_reshaped, ax=axs[1], color='blue').set(title='Humidity vs Rentals')
    sns.scatterplot(x='windspeed', y='cnt', data=df_reshaped, ax=axs[2], color='green').set(title='Windspeed vs Rentals')
    st.pyplot(fig)

st.sidebar.title("Menu Navigasi")
menu = st.sidebar.selectbox("Pilih Menu: ", ["Home"])
