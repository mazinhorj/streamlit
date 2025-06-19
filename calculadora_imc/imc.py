import streamlit as st

# Configurações iniciais
st.set_page_config(
    page_title="Calculadora de IMC",
    page_icon="⚖️"  # emoji de balança
)

with st.sidebar:
    st.title("Calculadora de IMC")
    st.write("Calcule seu Índice de Masa Corporal (IMC)")

    st.header("Sobre o IMC")
    st.write("""O Índice de Massa Corporal (IMC) é uma medida utilizada para avaliar se uma pessoa está com peso adequado, sobrepeso ou obesidade. 
    É calculado dividindo o peso (em kg) pela altura (em metros) ao quadrado. 
    O IMC é uma ferramenta útil, mas não substitui a avaliação médica. 
    Consulte sempre um profissional de saúde para uma análise mais completa.""")

# Tabela de classificação do IMC
imc_tabela = {
    (0, 18.5): "Abaixo do peso",
    (18.5, 24.9): "Peso normal",
    (25.0, 29.9): "Sobrepeso",
    (30.0, 34.9): "Obesidade grau I",
    (35.0, 39.9): "Obesidade grau II",
    (40.0, float('inf')): "Obesidade grau III"
}

# Função para classificar o IMC
def classificar_imc(imc):
    for (inicio, fim), categoria in imc_tabela.items():
        if inicio <= imc <= fim:
            return categoria
    return "Valor de IMC inválido"

# Inputs
st.title("Calculadora")
peso = st.number_input("Digite seu peso (kg)", min_value=1.0, step=0.1)
altura = st.number_input("Digite sua altura (m)", min_value=0.1, step=0.01)

if st.button("Calcular IMC"):
    if peso > 0 and altura > 0:
        imc = peso / (altura ** 2)
        st.success(f"Su IMC é: {imc:.2f}")
        st.write(f"Classificação: {classificar_imc(imc)}")     
    else:
        st.error("Por favor, digite valores válidos para peso e altura.")


st.divider()
# Exibir gráfico de IMC
st.image("https://www.laboranalise.com.br/wp-content/uploads/2016/02/tabela-imc.png", caption="https://www.laboranalise.com.br/wp-content/uploads/2016/02/tabela-imc.png")

# Exibir tabela de classificação do IMC
st.divider()
st.header("Tabela de Classificação do IMC")
col1, col2 = st.columns(2)

col1.metric("", "IMC")
for (inicio, fim), categoria in imc_tabela.items():
    col1.metric(f"", f"{inicio} - {fim}")
col2.metric(" ", 'Categoria')
for (inicio, fim), categoria in imc_tabela.items():
    col2.metric(f"", f"{categoria}")