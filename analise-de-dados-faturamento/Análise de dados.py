import pandas as pd
import plotly_express as px

# importa dados
dados = pd.read_csv("data.csv", encoding="iso-8859-1")
print(dados.head(10))       # 10 primeiras linhas
print(dados.tail(10))       # 10 ultimas linhas
print(dados.shape)          # número de linhas e colunas
print(dados.dtypes)         # verifica o tipo de dado das colunas
print(dados.describe())     # estatísticas

# análises
print(dados.Description.value_counts().to_frame())              # numero de pedidos por produto
print(dados.Country.value_counts().to_frame())                  # numero de pedidos por país
print(dados.groupby(["Country", "Description"]).UnitPrice.sum().to_frame())

# faturamento total
dados['Faturamento'] = dados['Quantity'] * dados['UnitPrice']
faturamento_total = dados['Faturamento'].sum()
print("Faturamento Total:", faturamento_total)

# faturamento por país
print(dados.groupby("Country").Faturamento.sum().to_frame())
print(dados.groupby("Country").Faturamento.sum().to_excel("Análise de faturamento.xlsx"))   # cria excel

# visualização de dados
grafico = px.histogram(dados, x="Country", y="Faturamento", text_auto=True, color="Description")
grafico.write_html("Gráfico faturamento.html")

# colunas = ["Description", "InvoiceDate", "Country"]
# for coluna in colunas:
#     grafico = px.histogram(dados, x=coluna, y="Faturamento", text_auto=True, color="Description")
#     grafico.show()
#     grafico.write_html(f"Faturamento por {coluna}.html")