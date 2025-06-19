import csv
import random
from datetime import datetime, timedelta
import faker

# Configuração inicial
fake = faker.Faker('pt_BR')
random.seed(42)
total_vendas = 1000

# Dados fixos para consistência
categorias = ['Eletrônicos', 'Roupas', 'Alimentos', 'Casa', 'Telefonia', 'Livros', 'Esportes', 'Beleza']
formas_pagamento = ['Cartão de Crédito', 'PIX', 'Boleto', 'Dinheiro', 'Cartão Débito']
canais_venda = ['Loja Online', 'Loja Física', 'Marketplace', 'Redes Sociais']
estados_brasil = ['SP', 'RJ', 'MG', 'RS', 'PR', 'SC', 'BA', 'DF']
status_entrega = ['Entregue', 'Em Trânsito', 'Processando', 'Devolvido']
vendedores = [{'id': i, 'nome': fake.name()} for i in range(1, 21)]

# Gerar produtos fictícios
produtos = []
for i in range(1, 51):
    categoria = random.choice(categorias)
    margem_preco = {
        'Eletrônicos': (50, 5000),
        'Roupas': (30, 400),
        'Alimentos': (5, 150),
        'Casa': (20, 800),
        'Telefonia': (100, 3000),
        'Livros': (15, 120),
        'Esportes': (40, 600),
        'Beleza': (10, 300)
    }
    preco_min, preco_max = margem_preco[categoria]
    produtos.append({
        'id': i,
        'nome': fake.catch_phrase(),
        'categoria': categoria,
        'preco': round(random.uniform(preco_min, preco_max), 2)
    })

# Função para gerar data aleatória no último ano
def random_date():
    end_date = datetime.now()
    start_date = end_date - timedelta(days=365)
    random_date = start_date + timedelta(
        seconds=random.randint(0, int((end_date - start_date).total_seconds())))
    return random_date.date(), random_date.time().strftime('%H:%M:%S')

# Gerar vendas
vendas = []
for i in range(1, total_vendas + 1):
    data, hora = random_date()
    cliente = {'id': random.randint(1000, 9999), 'nome': fake.name(), 'email': fake.email(), 
            'estado': random.choice(estados_brasil), 'cidade': fake.city()}
    
    # Selecionar 1-3 produtos por venda
    num_produtos = random.randint(1, 3)
    produtos_venda = random.sample(produtos, num_produtos)
    for produto in produtos_venda:
        produto['quantidade'] = random.randint(1, 5)
    
    valor_total = sum(p['preco'] * p['quantidade'] for p in produtos_venda)
    desconto = round(random.uniform(0, 0.2) * valor_total, 2) if random.random() > 0.7 else 0
    forma_pagamento_escolhida = random.choice(formas_pagamento)
    parcelas = random.randint(1, 12) if forma_pagamento_escolhida == 'Cartão de Crédito' else 1
    
    venda = {
        'id_venda': i,
        'data': data,
        'hora': hora,
        'valor_total': round(valor_total - desconto, 2),
        'desconto': desconto,
        'forma_pagamento': forma_pagamento_escolhida,
        'parcelas': parcelas,
        'id_cliente': cliente['id'],
        'nome_cliente': cliente['nome'],
        'email_cliente': cliente['email'],
        'estado_cliente': cliente['estado'],
        'cidade_cliente': cliente['cidade'],
        'id_produto': produtos_venda[0]['id'],
        'nome_produto': produtos_venda[0]['nome'],
        'categoria_produto': produtos_venda[0]['categoria'],
        'preco_unitario': produtos_venda[0]['preco'],
        'quantidade': produtos_venda[0]['quantidade'],
        'id_vendedor': random.choice(vendedores)['id'],
        'nome_vendedor': random.choice(vendedores)['nome'],
        'canal_venda': random.choice(canais_venda),
        'status_entrega': random.choice(status_entrega),
        'tempo_entrega_dias': random.randint(1, 15),
        'custo_frete': round(random.uniform(0, 30), 2) if random.random() > 0.4 else 0
    }
    
    vendas.append(venda)

# Escrever no arquivo CSV
cabecalho = vendas[0].keys()
with open('vendas_1000.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=cabecalho)
    writer.writeheader()
    writer.writerows(vendas)

print(f"Arquivo 'vendas_1000.csv' gerado com {total_vendas} registros.")