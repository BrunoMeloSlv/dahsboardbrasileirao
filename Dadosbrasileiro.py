#Selecione o folder
#.\footstats\Scripts\activate
#streamlit run footstats_st.py

import streamlit as st
import pandas as pd #pandas==2.0.2
import plotly.express as px #plotly==5.15.0


######### Importando a base



st.set_page_config(layout = 'wide')


st.title('Dashboard Brasileirão 2023 ⚽')


url = 'https://raw.githubusercontent.com/BrunoMeloSlv/DahsboardBrasileirao/main/dados2023.csv'
dados = pd.read_csv(url, sep=';')



st.sidebar.title('Filtros')



filtro_equipe = st.sidebar.multiselect('Equipe', dados['Equipe'].unique())
if filtro_equipe:
    dados = dados[dados['Equipe'].isin(filtro_equipe)]

#### Tabelas

#Jogador

jogos =  dados[['Equipe','Jogador','Jogos']].reset_index().sort_values('Jogos', ascending=False)
Passe =  dados[['Equipe','Jogador','Passe certo']].reset_index().sort_values('Passe certo', ascending=False)
Finalização =  dados[['Equipe','Jogador','Finalização certa']].reset_index().sort_values('Finalização certa', ascending=False)
Desarme =  dados[['Equipe','Jogador','Desarme certo']].reset_index().sort_values('Desarme certo', ascending=False)
Cruzamento =  dados[['Equipe','Jogador','Cruzamento certo']].reset_index().sort_values('Cruzamento certo', ascending=False)
Interceptação =  dados[['Equipe','Jogador','Interceptação certa']].reset_index().sort_values('Interceptação certa', ascending=False)
Dribles =  dados[['Equipe','Jogador','Dribles']].reset_index().sort_values('Dribles', ascending=False)
Virada  =  dados[['Equipe','Jogador','Virada de jogo certa']].reset_index().sort_values('Virada de jogo certa', ascending=False)
Gols =  dados[['Equipe','Jogador','Gols']].reset_index().sort_values('Gols', ascending=False)
Assistência_gol =  dados[['Equipe','Jogador','Assistência gol']].reset_index().sort_values('Assistência gol', ascending=False)
Assistência_finalização =  dados[['Equipe','Jogador','Assistência finalização']].reset_index().sort_values('Assistência finalização', ascending=False)
Defesa =  dados[['Equipe','Jogador','Defesa']].reset_index().sort_values('Defesa', ascending=False)
Defesa_difícil =  dados[['Equipe','Jogador','Defesa difícil']].reset_index().sort_values('Defesa difícil', ascending=False)
Rebatida =  dados[['Equipe','Jogador','Rebatida']].reset_index().sort_values('Rebatida', ascending=False)
Falta_cometida =  dados[['Equipe','Jogador','Falta cometida']].reset_index().sort_values('Falta cometida', ascending=False)
Falta_recebida =  dados[['Equipe','Jogador','Falta recebida']].reset_index().sort_values('Falta recebida', ascending=False)
Impedimentos =  dados[['Equipe','Jogador','Impedimentos']].reset_index().sort_values('Impedimentos', ascending=False)
Pênaltis_sofridos =  dados[['Equipe','Jogador','Pênaltis sofridos']].reset_index().sort_values('Pênaltis sofridos', ascending=False)
Pênaltis_cometidos =  dados[['Equipe','Jogador','Pênaltis cometidos']].reset_index().sort_values('Pênaltis cometidos', ascending=False)
Perda_da_posse =  dados[['Equipe','Jogador','Perda da posse de bola']].reset_index().sort_values('Perda da posse de bola', ascending=False)
Cartão_vermelho =  dados[['Equipe','Jogador','Cartão vermelho']].reset_index().sort_values('Cartão vermelho', ascending=False)
Cartão_amarelo =  dados[['Equipe','Jogador','Cartão amarelo']].reset_index().sort_values('Cartão amarelo', ascending=False)

# Times

time_passes = pd.DataFrame(dados.groupby('Equipe')['Passe certo'].sum()).reset_index().sort_values('Passe certo', ascending=False)
time_Finalização = pd.DataFrame(dados.groupby('Equipe')['Finalização certa'].sum()).reset_index().sort_values('Finalização certa', ascending=False)
time_desarmes = pd.DataFrame(dados.groupby('Equipe')['Desarme certo'].sum()).reset_index().sort_values('Desarme certo', ascending=False)
time_Cruzamento = pd.DataFrame(dados.groupby('Equipe')['Cruzamento certo'].sum()).reset_index().sort_values('Cruzamento certo', ascending=False)
time_Interceptação = pd.DataFrame(dados.groupby('Equipe')['Interceptação certa'].sum()).reset_index().sort_values('Interceptação certa', ascending=False)
time_Dribles = pd.DataFrame(dados.groupby('Equipe')['Dribles'].sum()).reset_index().sort_values('Dribles', ascending=False)
time_Virada = pd.DataFrame(dados.groupby('Equipe')['Virada de jogo certa'].sum()).reset_index().sort_values('Virada de jogo certa', ascending=False)
time_Gols = pd.DataFrame(dados.groupby('Equipe')['Gols'].sum()).reset_index().sort_values('Gols', ascending=False)
time_Assistência_gol = pd.DataFrame(dados.groupby('Equipe')['Assistência gol'].sum()).reset_index().sort_values('Assistência gol', ascending=False)
time_Assistência_finalização = pd.DataFrame(dados.groupby('Equipe')['Assistência finalização'].sum()).reset_index().sort_values('Assistência finalização', ascending=False)
time_Defesa = pd.DataFrame(dados.groupby('Equipe')['Defesa'].sum()).reset_index().sort_values('Defesa', ascending=False)
time_Defesa_difícil = pd.DataFrame(dados.groupby('Equipe')['Defesa difícil'].sum()).reset_index().sort_values('Defesa difícil', ascending=False)
time_Rebatida = pd.DataFrame(dados.groupby('Equipe')['Rebatida'].sum()).reset_index().sort_values('Rebatida', ascending=False)
time_Falta_cometida = pd.DataFrame(dados.groupby('Equipe')['Falta cometida'].sum()).reset_index().sort_values('Falta cometida', ascending=False)
time_Falta_recebida = pd.DataFrame(dados.groupby('Equipe')['Falta recebida'].sum()).reset_index().sort_values('Falta recebida', ascending=False)
time_Impedimentos = pd.DataFrame(dados.groupby('Equipe')['Impedimentos'].sum()).reset_index().sort_values('Impedimentos', ascending=False)
time_Pênaltis_sofridos = pd.DataFrame(dados.groupby('Equipe')['Pênaltis sofridos'].sum()).reset_index().sort_values('Pênaltis sofridos', ascending=False)
time_Pênaltis_cometidos = pd.DataFrame(dados.groupby('Equipe')['Pênaltis cometidos'].sum()).reset_index().sort_values('Pênaltis cometidos', ascending=False)
time_Cartão_vermelho = pd.DataFrame(dados.groupby('Equipe')['Cartão vermelho'].sum()).reset_index().sort_values('Cartão vermelho', ascending=False)
time_Cartão_amarelo = pd.DataFrame(dados.groupby('Equipe')['Cartão amarelo'].sum()).reset_index().sort_values('Cartão amarelo', ascending=False)

dados_agrupados = pd.merge(time_Finalização, time_Gols, left_on = 'Equipe', right_on = 'Equipe')

### Gráficos

### Jogador

fig_Jogos = px.bar(jogos.head(),
                             x = 'Jogador',
                             y = 'Jogos',
                             text_auto= True,
                             title= 'Top Nº de Jogos')
fig_Jogos.update_layout(yaxis_title = 'Jogos')

fig_Passe = px.bar(Passe.head(),
                             x = 'Jogador',
                             y = 'Passe certo',
                             text_auto= True,
                             title= 'Top Nº de Passes certos')
fig_Passe.update_layout(yaxis_title = 'Passes certos')

fig_Finalização = px.bar(Finalização.head(),
                             x = 'Jogador',
                             y = 'Finalização certa',
                             text_auto= True,
                             title= 'Top Nº de Finalizações certas')
fig_Finalização.update_layout(yaxis_title = 'Finalizações certas')

fig_Desarme = px.bar(Desarme.head(),
                             x = 'Jogador',
                             y = 'Desarme certo',
                             text_auto= True,
                             title= 'Top Nº de Desarmes certos')
fig_Desarme.update_layout(yaxis_title = 'Desarmes certos')

fig_Cruzamento = px.bar(Cruzamento.head(),
                             x = 'Jogador',
                             y = 'Cruzamento certo',
                             text_auto= True,
                             title= 'Top Nº de Cruzamentos certos')
fig_Cruzamento.update_layout(yaxis_title = 'Cruzamentos certos')

fig_Interceptação = px.bar(Interceptação.head(),
                             x = 'Jogador',
                             y = 'Interceptação certa',
                             text_auto= True,
                             title= 'Top Nº de Interceptações certas')
fig_Interceptação.update_layout(yaxis_title = 'Interceptações certas')

fig_Dribles = px.bar(Dribles.head(),
                             x = 'Jogador',
                             y = 'Dribles',
                             text_auto= True,
                             title= 'Top Nº de Dribles certos')
fig_Dribles.update_layout(yaxis_title = 'Dribles certos')

fig_Virada = px.bar(Virada.head(),
                             x = 'Jogador',
                             y = 'Virada de jogo certa',
                             text_auto= True,
                             title= 'Top Nº de Viradas de jogo certas')
fig_Virada.update_layout(yaxis_title = 'Viradas de jogo')

fig_Gols = px.bar(Gols.head(),
                             x = 'Jogador',
                             y = 'Gols',
                             text_auto= True,
                             title= 'Top Nº de Gols')
fig_Gols.update_layout(yaxis_title = 'Gols')

fig_Assistências_Gols = px.bar(Assistência_gol.head(),
                             x = 'Jogador',
                             y = 'Assistência gol',
                             text_auto= True,
                             title= 'Top Nº de Assistências para gol')
fig_Assistências_Gols.update_layout(yaxis_title = 'Assistências')

fig_Assistência_finalização = px.bar(Assistência_finalização.head(),
                             x = 'Jogador',
                             y = 'Assistência finalização',
                             text_auto= True,
                             title= 'Top Nº de Assistências para finalização')
fig_Assistência_finalização.update_layout(yaxis_title = 'Assistência finalização')

fig_Defesa_difícil = px.bar(Defesa_difícil.head(),
                             x = 'Jogador',
                             y = 'Defesa difícil',
                             text_auto= True,
                             title= 'Top Nº de Defesas difíceis')
fig_Defesa_difícil.update_layout(yaxis_title = 'Defesas')

fig_Defesa = px.bar(Defesa.head(),
                             x = 'Jogador',
                             y = 'Defesa',
                             text_auto= True,
                             title= 'Top Nº de Defesas')
fig_Defesa.update_layout(yaxis_title = 'Defesa')

fig_Rebatida = px.bar(Rebatida.head(),
                             x = 'Jogador',
                             y = 'Rebatida',
                             text_auto= True,
                             title= 'Top Nº de Rebatidas')
fig_Rebatida.update_layout(yaxis_title = 'Rebatida')

fig_Falta_cometida = px.bar(Falta_cometida.head(),
                             x = 'Jogador',
                             y = 'Falta cometida',
                             text_auto= True,
                             title= 'Top Nº de Faltas cometidas')
fig_Falta_cometida.update_layout(yaxis_title = 'Faltas')

fig_Falta_recebida = px.bar(Falta_recebida.head(),
                             x = 'Jogador',
                             y = 'Falta recebida',
                             text_auto= True,
                             title= 'Top Nº de Faltas recebidas')
fig_Falta_recebida.update_layout(yaxis_title = 'Faltas')

fig_Impedimentos = px.bar(Impedimentos.head(),
                             x = 'Jogador',
                             y = 'Impedimentos',
                             text_auto= True,
                             title= 'Top Nº de Impedimentos')
fig_Impedimentos.update_layout(yaxis_title = 'Impedimentos')

fig_Pênaltis_sofridos = px.bar(Pênaltis_sofridos.head(),
                             x = 'Jogador',
                             y = 'Pênaltis sofridos',
                             text_auto= True,
                             title= 'Top Nº de Pênaltis sofridos')
fig_Pênaltis_sofridos.update_layout(yaxis_title = 'Pênaltis')

fig_Pênaltis_cometidos = px.bar(Pênaltis_cometidos.head(),
                             x = 'Jogador',
                             y = 'Pênaltis cometidos',
                             text_auto= True,
                             title= 'Top Nº de Pênaltis cometidos')
fig_Pênaltis_cometidos.update_layout(yaxis_title = 'Pênaltis')

fig_Perda_da_posse = px.bar(Perda_da_posse.head(),
                             x = 'Jogador',
                             y = 'Perda da posse de bola',
                             text_auto= True,
                             title= 'Top Nº de Perda da posse de bola')
fig_Perda_da_posse.update_layout(yaxis_title = 'Perda de Posse')

fig_Cartão_vermelho = px.bar(Cartão_vermelho.head(),
                             x = 'Jogador',
                             y = 'Cartão vermelho',
                             text_auto= True,
                             title= 'Top Nº de Cartões vermelhos')
fig_Cartão_vermelho.update_layout(yaxis_title = 'Cartões vermelhos')

fig_Cartão_amarelo = px.bar(Cartão_amarelo.head(),
                             x = 'Jogador',
                             y = 'Cartão amarelo',
                             text_auto= True,
                             title= 'Top Nº de Cartões amarelos')
fig_Cartão_amarelo.update_layout(yaxis_title = 'Cartões amarelos')

## Times

fig_teste =  px.scatter(data_frame = dados_agrupados, x = 'Finalização certa', y = 'Gols', text = 'Equipe', size = 'Gols')
fig_teste.update_layout(yaxis_title = 'Gols')

fig_time_passes = px.bar(time_passes.head(),
                             x = 'Equipe',
                             y = 'Passe certo',
                             text_auto= True,
                             title= 'Top Nº de Passes certos')
fig_time_passes.update_layout(yaxis_title = 'Passes certos')


fig_time_Finalização = px.bar(time_Finalização.head(),
                             x = 'Equipe',
                             y = 'Finalização certa',
                             text_auto= True,
                             title= 'Top Nº de Finalizações certas')
fig_time_Finalização.update_layout(yaxis_title = 'Finalizações')

fig_time_Desarme = px.bar(time_desarmes.head(),
                             x = 'Equipe',
                             y = 'Desarme certo',
                             text_auto= True,
                             title= 'Top Nº de Desarmes certos')
fig_time_Desarme.update_layout(yaxis_title = 'Desarmes certos')

fig_time_Cruzamento = px.bar(time_Cruzamento.head(),
                             x = 'Equipe',
                             y = 'Cruzamento certo',
                             text_auto= True,
                             title= 'Top Nº de Cruzamentos certos')
fig_time_Cruzamento.update_layout(yaxis_title = 'Cruzamentos certos')

fig_time_Interceptação = px.bar(time_Interceptação.head(),
                             x = 'Equipe',
                             y = 'Interceptação certa',
                             text_auto= True,
                             title= 'Top Nº de Interceptações certas')
fig_time_Interceptação.update_layout(yaxis_title = 'Interceptações certas')

fig_time_Dribles = px.bar(time_Dribles.head(),
                             x = 'Equipe',
                             y = 'Dribles',
                             text_auto= True,
                             title= 'Top Nº de Dribles certos')
fig_time_Dribles.update_layout(yaxis_title = 'Dribles certos')

fig_time_Virada = px.bar(time_Virada.head(),
                             x = 'Equipe',
                             y = 'Virada de jogo certa',
                             text_auto= True,
                             title= 'Top Nº de Viradas de jogo certas')
fig_time_Virada.update_layout(yaxis_title = 'Viradas de jogo')

fig_time_Gols = px.bar(time_Gols.head(),
                             x = 'Equipe',
                             y = 'Gols',
                             text_auto= True,
                             title= 'Top Nº de Gols')
fig_time_Gols.update_layout(yaxis_title = 'Gols')

fig_time_Assistência_gol = px.bar(time_Assistência_gol.head(),
                             x = 'Equipe',
                             y = 'Assistência gol',
                             text_auto= True,
                             title= 'Top Nº de Assistências para gol')
fig_time_Assistência_gol.update_layout(yaxis_title = 'Assistências')

fig_time_Assistência_finalização = px.bar(time_Assistência_finalização.head(),
                             x = 'Equipe',
                             y = 'Assistência finalização',
                             text_auto= True,
                             title= 'Top Nº de Assistências para finalização')
fig_time_Assistência_finalização.update_layout(yaxis_title = 'Assistência finalização')

fig_time_Defesa_difícil = px.bar(time_Defesa_difícil.head(),
                             x = 'Equipe',
                             y = 'Defesa difícil',
                             text_auto= True,
                             title= 'Top Nº de Defesas difíceis')
fig_time_Defesa_difícil.update_layout(yaxis_title = 'Defesas')

fig_time_Defesa = px.bar(time_Defesa.head(),
                             x = 'Equipe',
                             y = 'Defesa',
                             text_auto= True,
                             title= 'Top Nº de Defesas')
fig_time_Defesa.update_layout(yaxis_title = 'Defesa')

fig_time_Rebatida = px.bar(time_Rebatida.head(),
                             x = 'Equipe',
                             y = 'Rebatida',
                             text_auto= True,
                             title= 'Top Nº de Rebatidas')
fig_time_Rebatida.update_layout(yaxis_title = 'Rebatida')

fig_time_Falta_cometida = px.bar(time_Falta_cometida.head(),
                             x = 'Equipe',
                             y = 'Falta cometida',
                             text_auto= True,
                             title= 'Top Nº de Faltas cometidas')
fig_time_Falta_cometida.update_layout(yaxis_title = 'Faltas')

fig_time_Falta_recebida = px.bar(time_Falta_recebida.head(),
                             x = 'Equipe',
                             y = 'Falta recebida',
                             text_auto= True,
                             title= 'Top Nº de Faltas recebidas')
fig_time_Falta_recebida.update_layout(yaxis_title = 'Faltas')

fig_time_Impedimentos = px.bar(time_Impedimentos.head(),
                             x = 'Equipe',
                             y = 'Impedimentos',
                             text_auto= True,
                             title= 'Top Nº de Impedimentos')
fig_time_Impedimentos.update_layout(yaxis_title = 'Impedimentos')

fig_time_Pênaltis_sofridos = px.bar(time_Pênaltis_sofridos.head(),
                             x = 'Equipe',
                             y = 'Pênaltis sofridos',
                             text_auto= True,
                             title= 'Top Nº de Pênaltis sofridos')
fig_time_Pênaltis_sofridos.update_layout(yaxis_title = 'Pênaltis')

fig_time_Pênaltis_cometidos = px.bar(time_Pênaltis_cometidos.head(),
                             x = 'Equipe',
                             y = 'Pênaltis cometidos',
                             text_auto= True,
                             title= 'Top Nº de Pênaltis cometidos')
fig_time_Pênaltis_cometidos.update_layout(yaxis_title = 'Pênaltis')

fig_time_Cartão_vermelho = px.bar(time_Cartão_vermelho.head(),
                             x = 'Equipe',
                             y = 'Cartão vermelho',
                             text_auto= True,
                             title= 'Top Nº de Cartões vermelhos')
fig_time_Cartão_vermelho.update_layout(yaxis_title = 'Cartões vermelhos')

fig_time_Cartão_amarelo = px.bar(time_Cartão_amarelo.head(),
                             x = 'Equipe',
                             y = 'Cartão amarelo',
                             text_auto= True,
                             title= 'Top Nº de Cartões amarelos')
fig_time_Cartão_amarelo.update_layout(yaxis_title = 'Cartões amarelos')


## Visualização
aba1, aba2 = st.tabs(['Jogador', 'Times'])
with aba1:
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(fig_Jogos,use_container_width= True)
        st.plotly_chart(fig_Finalização,use_container_width= True)
        st.plotly_chart(fig_Cruzamento,use_container_width= True)
        st.plotly_chart(fig_Dribles,use_container_width= True)
        st.plotly_chart(fig_Gols,use_container_width= True)
        st.plotly_chart(fig_Assistência_finalização,use_container_width= True)
        st.plotly_chart(fig_Defesa,use_container_width= True)
        st.plotly_chart(fig_Falta_cometida,use_container_width= True)
        st.plotly_chart(fig_Impedimentos,use_container_width= True)
        st.plotly_chart(fig_Pênaltis_cometidos,use_container_width= True)
        st.plotly_chart(fig_Cartão_vermelho,use_container_width= True)

    with col2:
        st.plotly_chart(fig_Passe,use_container_width= True)
        st.plotly_chart(fig_Desarme,use_container_width= True)
        st.plotly_chart(fig_Interceptação,use_container_width= True)
        st.plotly_chart(fig_Virada,use_container_width= True)
        st.plotly_chart(fig_Assistências_Gols,use_container_width= True)
        st.plotly_chart(fig_Defesa_difícil,use_container_width= True)
        st.plotly_chart(fig_Rebatida,use_container_width= True)
        st.plotly_chart(fig_Falta_recebida,use_container_width= True)
        st.plotly_chart(fig_Pênaltis_sofridos,use_container_width= True)
        st.plotly_chart(fig_Perda_da_posse,use_container_width= True)
        st.plotly_chart(fig_Cartão_amarelo,use_container_width= True)

with aba2:
    col1, col2 = st.columns(2)
    with col1:
       st.plotly_chart(fig_time_passes,use_container_width= True)
       st.plotly_chart(fig_time_Desarme,use_container_width= True)
       st.plotly_chart(fig_time_Interceptação,use_container_width= True)
       st.plotly_chart(fig_time_Assistência_gol,use_container_width= True)
       st.plotly_chart(fig_time_Defesa_difícil,use_container_width= True)
       st.plotly_chart(fig_time_Rebatida,use_container_width= True)
       st.plotly_chart(fig_time_Falta_recebida,use_container_width= True)
       st.plotly_chart(fig_time_Impedimentos,use_container_width= True)
       st.plotly_chart(fig_time_Pênaltis_cometidos,use_container_width= True)
       st.plotly_chart(fig_time_Cartão_amarelo,use_container_width= True)
       st.plotly_chart(fig_teste,use_container_width= True)
 
    with col2:
        st.plotly_chart(fig_time_Finalização,use_container_width= True)
        st.plotly_chart(fig_time_Cruzamento,use_container_width= True)
        st.plotly_chart(fig_time_Dribles,use_container_width= True)
        st.plotly_chart(fig_time_Gols,use_container_width= True)
        st.plotly_chart(fig_time_Assistência_finalização,use_container_width= True)
        st.plotly_chart(fig_time_Defesa,use_container_width= True)
        st.plotly_chart(fig_time_Falta_cometida,use_container_width= True)
        st.plotly_chart(fig_time_Impedimentos,use_container_width= True)
        st.plotly_chart(fig_time_Pênaltis_sofridos,use_container_width= True)
        st.plotly_chart(fig_time_Cartão_vermelho,use_container_width= True)



        
