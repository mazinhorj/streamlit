import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Análise de dados de vendas",
    page_icon="💰",  # emojis de dinheiro
    layout="wide"  # layout da página
)

with st.sidebar:
    st.title("Análise de Vendas")
    st.write("Análise de dados de vendas de uma loja fictícia")

    st.header("Sobre a análise")
    st.write("""Esta análise utiliza um conjunto de dados fictício de vendas para demonstrar como realizar análises exploratórias, visualizações e insights sobre o desempenho das vendas. O objetivo é entender melhor os padrões de compra, sazonalidade e outros fatores que afetam as vendas.""")

    # Carregar os dados
    uploaded_file = st.file_uploader("Carregar arquivo CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    with st.sidebar:
        st.success("Arquivo carregado com sucesso!")

        ditinct_estados = df['estado_cliente'].unique().tolist()
        estado_selecionado = st.selectbox("Selecione um estado", ditinct_estados)

        vendedor_selecionado = st.radio("Selecione um vendedor", df['nome_vendedor'].unique())

        if estado_selecionado:
                df = df[df['estado_cliente'] == estado_selecionado]

        if vendedor_selecionado:
                df = df[df['nome_vendedor'] == vendedor_selecionado]

    
    st.dataframe(df, use_container_width=True)

    st.write(f"Total de vendas: R$ {df['valor_total'].sum():.2f}")
    st.write(f"Número de vendas: {df.shape[0]}")
    st.write(f"Estado selecionado: {estado_selecionado}")
    st.write(f"Vendedor selecionado: {vendedor_selecionado}")

    st.bar_chart(df, x='nome_cliente', y='valor_total', use_container_width=True)

else:
    st.warning("Por favor, carregue um arquivo CSV para análise.")
    df = pd.DataFrame()
