import streamlit as st
import pandas as pd
import plotly.express as px
import sqlalchemy as db
import matplotlib.pyplot as plt
import missingno as msno
import numpy as np
import math
import statistics
import seaborn as sns
from datetime import date

import warnings
warnings.filterwarnings('ignore')


engine = db.create_engine('sqlite:///bancodedados.db', echo = True)

st.image('4_scripts/logo.png', caption='',width = 100)

st.write('**Global unemployment Watch**')


st.sidebar.header('quantidade de desemprego dos meses por ano')

df = pd.read_sql('bancodedado.db', con=engine)
pais = df['ano'].drop_duplicates()


opcao = st.selectbox(
    'Escolha um mes:',
    ['Taxa de desemprego em jan', 'Taxa de desemprego em Fev', 'Taxa de desemprego em Mar','Taxa de desemprego em Abr']
)
st.write(f'Você selecionou: {opcao}')


st.write(opcao)
fig = px.scatter(df,'ano',opcao)
st.plotly_chart(fig)
fig1 = px.bar(df, x='ano', y=opcao)
st.plotly_chart(fig1)

fig2 = px.pie(df,'Taxa de desemprego em jan','ano')
st.plotly_chart(fig2)

