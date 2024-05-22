import pandas as pd

url = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/base-de-dados/aluguel.csv'

url_alunos = 'https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv'

dados = pd.read_csv(url, sep=';')

df_alunos = pd.read_csv(url_alunos)

# dados.groupby('Tipo').mean(numeric_only=True)    # numeric_only=True evita erro de execução

# dados.groupby('Tipo')['Valor'].mean()            # declarar ["Valor"] antes de .mean() exclui a necessidade de numeric_only=True 
                                                   # já que valor é numeric

dados.groupby('Tipo')[['Valor']].mean().sort_values("Valor")            # Colchetes duplos faz com que transforme a seleção em um DataFrame ao invés de series
                                                                        # sort_values ordena os valores a partir de uma coluna que precisa ser especificada

df_preco_tipo = dados.groupby('Tipo')[['Valor']].mean().sort_values("Valor")
df_preco_tipo.plot(kind='barh', figsize=(14, 10))

# Remoção de imovéis não-residenciais
dados.Tipo.unique()

imoveis_comerciais = [
   'Conjunto Comercial/Sala',
   'Prédio Inteiro', 'Loja/Salão',
   'Galpão/Depósito/Armazém',
   'Casa Comercial', 'Terreno Padrão',
   'Loja Shopping/ Ct Comercial',
   'Box/Garagem', 'Chácara',
   'Loteamento/Condomínio', 'Sítio',
   'Pousada/Chalé', 'Hotel', 'Indústria'
]

df = dados.query('@imoveis_comerciais not in Tipo')
df.Tipo.unique()

df_preco_tipo = df.groupby('Tipo')[['Valor']].mean().sort_values("Valor")
df_preco_tipo.plot(kind='barh', figsize=(14, 10))

# Qual o percentual de cada tipo de imóvel na nossa base de dados?

df_percentual_tipo = df.Tipo.value_counts(normalize=True).to_frame().sort_values('proportion')
df_percentual_tipo.plot(kind='bar', figsize=(14, 10), color='green',
                        xlabel='Tipos', ylabel='Percentual')

#selecionando apenas os imíveis do tipo apartamento
df = df.query('Tipo == "Apartamento"')

# Tratando os valores nulos

df.isnull().sum()

df = df.fillna(0) 

# Removendo registros
registros_a_remover = df.query('Valor == 0 | Condominio == 0').index
df.drop(registros_a_remover, axis=0, inplace=True)