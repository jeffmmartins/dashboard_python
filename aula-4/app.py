#importar as bibliotecas 
import streamlit as st
import pandas as pd
import plotly.express as px

#configuração da página , define titulo , icone e tamanho
st.set_page_config(
    page_title="Dashboard de Salários na Área de dados",
    page_icon="📊",
    layout="wide"
)

#carregamento dos dados
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

##--Barra Lateral (filtros)--
st.sidebar.header("🔍 Filtros")

#Filtro do ano
anos_disponiveis = sorted(df["ano_trabalho"].unique())
anos_selecionados = st.sidebar.multiselect("Ano", anos_disponiveis,default=anos_disponiveis)