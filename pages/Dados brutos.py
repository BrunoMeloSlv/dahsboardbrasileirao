import streamlit as st
import requests
import pandas as pd

@st.cache_data
def converte_csv(df):
    return df.to_csv(index = False).encode('utf-8')

import time
def mensagem_sucesso():
    sucesso = st.success('Arquivo baixado com sucesso!', icon = "✅")
    time.sleep(5)
    sucesso.empty()

url = 'https://raw.githubusercontent.com/BrunoMeloSlv/DahsboardBrasileirao/main/dados2023.csv'
dados = pd.read_csv(url, sep=';')

filtro_equipe = st.sidebar.multiselect('Equipe', dados['Equipe'].unique())
if filtro_equipe:
    dados = dados[dados['Equipe'].isin(filtro_equipe)]

st.title('DADOS BRUTOS')

st.markdown(f'A tabela possui :blue[{dados.shape[0]}] linhas e :blue[{dados.shape[1]}] colunas')

with st.expander('Colunas'):
    colunas = st.multiselect('Selecione as colunas', list(dados.columns), list(dados.columns))

st.dataframe(dados)



st.markdown('Escreva um nome para o arquivo')
coluna1, coluna2 = st.columns(2)
with coluna1:
    nome_arquivo = st.text_input('', label_visibility = 'collapsed', value = 'dados')
    nome_arquivo += '.csv'
with coluna2:
    st.download_button('Fazer o download da tabela em csv', data = converte_csv(dados), file_name = nome_arquivo, mime = 'text/csv', on_click = mensagem_sucesso)
