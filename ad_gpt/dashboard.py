import streamlit as st
import pandas as pd
import os
from openai import OpenAI



st.title("AdGPT Dashboard")

arquivo = open('/home/mazinho/Documentos/streamlit/ad_gpt/vendas_1000.csv')

df = pd.read_csv(arquivo)

st.write("DataFrame:")
st.dataframe(df, use_container_width=True)

# metricas
st.subheader("Métricas")
st.metric(label="Total de Vendas", value=df['valor_total'].sum())
st.metric(label="total de produtos vendidos", value=df['quantidade'].sum())
st.metric(label="Média de Preço/Produto", value=(df['valor_total'].sum()/df['quantidade'].sum()).round(2))

# st.write("DataFrame Info:")
# info = df.describe()
# st.write(info.round(2)) 

# Gráfico de vendas por vendedor
st.subheader("Vendas por vendedor")
vendas_por_vendedor = df.groupby('nome_vendedor')['quantidade'].sum().reset_index()
vendas_por_vendedor = vendas_por_vendedor.sort_values(by='quantidade', ascending=True)
st.line_chart(vendas_por_vendedor.set_index('nome_vendedor'))  

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
model="gpt-3.5-turbo",
messages=[
    {"role": "developer", "content": "Você é um assistente amigável."},
    {"role": "user", "content": f"O dataset a seguir traz informações sobre vendas de uma determinada empresa. Analise os dados e gere 5 insights sobre o desempenho dos vendedores, produtos mais vendidos e outras métricas relevantes. {df}"},
]
)

st.markdown(completion.choices[0].message[0].content)