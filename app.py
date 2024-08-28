import streamlit as st
import pandas as pd
import os
import matplotlib.pyplot as plt

# Definir caminho relativo para o arquivo CSV
csv_path = 'mercadolivre/Dashboard/starturls.csv'

# Carregar dados CSV
df = pd.read_csv(csv_path)

# Título da aplicação
st.title('Web Scraping do Mercado Livre')

# Exibir dados no Streamlit para inspeção
st.write("Dados Carregados:")
st.write(df)  # Mostrar as primeiras linhas para verificar o formato dos dados

# Exibir os tipos de dados e os preços após a conversão
st.write("Tipos de Dados:")
st.write(df.dtypes)

# Verificar estatísticas básicas para checar valores inválidos
st.write("Estatísticas Descritivas dos Preços:")
st.write(df['price'].describe())



