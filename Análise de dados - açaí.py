import pandas as pd
import plotly_express as px

# importa dados
dados = pd.read_excel("vendas.xlsx")
print(dados.head(10))                               # 10 primeiras linhas
print(dados.tail(10))                               # 10 ultimas linhas
print(dados.shape)                                  # número de linhas e colunas
print(dados.dtypes)                                 # verifica o tipo de dado das colunas
print(dados.describe())                             # estatísticas
print(dados.loja)                                   # acessa uma coluna
print(dados.nunique())                              # valores únicos de uma coluna
print(dados.loja.value_counts())                    # contagem de valores de uma coluna
print(dados.loja.value_counts(normalize=True))      # contagem de valores de uma coluna valor relativo

# agrupamento de dados
print("\nFaturamento por loja:")
print(dados.groupby('loja').preco.sum())
print("\nFaturamento por loja (ticket médio):")
print(dados.groupby('loja').preco.mean())
print(dados.groupby(['estado', 'loja', 'forma_pagamento']).preco.sum().to_excel("Análise de faturamento.xlsx"))   # cria excel
print("\nPlanilha Excel criada")

# gráficos
grafico = px.histogram(dados, x="loja", color="regiao", text_auto=True)
grafico.write_html("Gráfico faturamento.html")
print("\nGráfico faturamento criado")

# múltiplos gráficos
colunas = ['loja', 'cidade', 'estado', 'tamanho', 'local_consumo']
for coluna in colunas:
    fig = px.histogram(dados, x=coluna, y='preco', color='forma_pagamento', text_auto=True)
    fig.write_html(f"Faturamento por {coluna}.html")
    print(f"Gráfico faturamento por {coluna} criado")