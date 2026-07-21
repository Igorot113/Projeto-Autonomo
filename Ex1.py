import pandas as pd
# C:\Users\Master-Data\AppData\Local\Python\pythoncore-3.14-64\Scripts
# Dados de exemplo
dados = {
    'Produto': ['Notebbok', 'Celular', 'Monitor','Teclado','HD2TB','Caneta'],
    'Categoria': ['Computador','Computador','Computador','Computador,Computador','Escritorio'],
    'Quantidade': [5,20,10,100,2,100],
    'Preço Unitario': [4500,2500,1200,150,10,1.50]
}

# Criando um dataFrame = Excel do python
df = pd.DataFrame(dados)

# Criando uma nova coluna de dados chamada Faturamento total onde faz o calculo da quantidade * preço unitario.
df['Faturamento Total'] = df['Quantidade']*df['Preço Unitario']

df.to_excel('relatorio_normal.xlsx')
df.to_excel('relatorio_normal_sem_index.xlsx',index=False)

# Filtrar dados (no caso produtos com faturamento maior que 2000)
df_filtrado = df[df['Faturamento Total'] > 2000]

# Salvando o resultado em um arquivo Excel
df_filtrado.to_excel('relatorio_filtrado.xlsx',index=False)
