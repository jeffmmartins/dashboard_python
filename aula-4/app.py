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
anos_disponiveis = sorted(df['work_year'].unique())
anos_selecionados = st.sidebar.multiselect("Ano", anos_disponiveis,default=anos_disponiveis)

# Filtro de Senioridade
senioridades_disponiveis = sorted(df['experience_level'].unique())
senioridades_selecionadas = st.sidebar.multiselect("Senioridade", senioridades_disponiveis, default=senioridades_disponiveis)

# Filtro por Tipo de Contrato
contratos_disponiveis = sorted(df['employment_type'].unique())
contratos_selecionados = st.sidebar.multiselect("Tipo de Contrato", contratos_disponiveis, default=contratos_disponiveis)

# Filtro por Tamanho da Empresa
tamanhos_disponiveis = sorted(df['company_size'].unique())
tamanhos_selecionados = st.sidebar.multiselect("Tamanho da Empresa", tamanhos_disponiveis, default=tamanhos_disponiveis)

#Filtragem do Datarame
#Dataframe principal é filtrado com base nas seleções feitas na barra lateral
df_filtrado= df[
    (df['work_year'].isin(anos_selecionados)) &
    (df["experience_level"].isin(senioridades_disponiveis)) &
    (df["employment_type"].isin(contratos_selecionados)) &
    (df["company_size"].isin(tamanhos_selecionados))
]
