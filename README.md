# ALURA Python Pandas - Conhecendo a Biblioteca

dados.head(int n = 5) retorna as n primeiras linhas de uma tabela
dados.tail(int n = 5) retorna as n últimas linhas de uma tabela


### read_csv


O Pandas fornece diversas funções para importar e exportar dados em diferentes formatos. As principais funções do Pandas para importar dados são as seguintes:

**read_csv():** Essa função é usada para ler arquivos CSV (Comma Separated Values), que são arquivos de texto que contêm dados separados por vírgulas. É possível passar diversos parâmetros para personalizar a leitura do csv, como delimitador, cabeçalho, tipo de encoding, entre outros.

**read_excel():** Essa função é usada para ler arquivos do Excel (.xls ou .xlsx) e criar um DataFrame a partir dos dados.

**read_json():** Essa função é usada para ler arquivos JSON (JavaScript Object Notation), que são arquivos de texto que contêm dados em formato de objeto JavaScript.

**read_html():** Essa função é usada para ler tabelas HTML, que são estruturas de dados organizadas em formato de tabela em uma página da web.

**read_sql():** Essa função é usada para ler dados de um banco de dados relacional, como o MySQL, PostgreSQL e SQL Server. O Pandas é capaz de importar dados de diferentes formas, permitindo ajustar parâmetros como a consulta, o nome da tabela e o tipo de dados das colunas.

**dados.shape** retorna (nº linhas, nº colunas)

o método **describe()** retorna as estatísticas descritivas básicas das variáveis numéricas de um dado conjunto tais como contagem, média, desvio, min, max, e quartis


### groupby()


A ideia por trás do groupby é dividir os dados em grupos com base nos critérios selecionados e, em seguida, aplicar uma operação a esses grupos. Essa operação pode ser uma função de agregação, como soma, média, contagem, desvio padrão, entre outras, ou mesmo uma operação personalizada definida pela pessoa usuária.

Esse método possui diversos parâmetros, alguns deles são:

by: esse é o parâmetro mais comum e é usado para especificar a coluna ou colunas que queremos agrupar. Como argumento dele, podemos passar o nome de uma coluna ou uma lista de nomes de colunas;

axis: utilizamos esse parâmetro para especificar o eixo ao longo do qual queremos agrupar. O valor padrão dele é 0, o que significa que as linhas serão agrupadas. Se quisermos agrupar as colunas, devemos definir esse parâmetro como 1;

sort: esse parâmetro é um booleano (True ou False) que indica se os grupos devem ser ordenados pelo valor da coluna de agrupamento. O valor padrão é True;

dropna: utilizamos esse parâmetro para controlar se os valores ausentes (NaN) serão excluídos ou não durante o processo de agrupamento. O valor padrão é True.


### Lidando com dados nulos


Existem diversas formas de tratar dados nulos com o Pandas. Algumas das principais formas são:

Remover os dados nulos: É possível remover as linhas ou colunas que possuem valores nulos utilizando o método dropna() . Esse método remove todas as linhas ou colunas que possuem pelo menos um valor nulo.

Preencher os dados nulos: Utilizando o método fillna(), podemos preencher os valores nulos com um valor específico. Além disso, também é possível utilizar argumentos específicos do método fillna() como o method=”ffill” ou method=”bfill” para preencher os valores nulos com o valor anterior ou posterior, respectivamente.

Interpolar os dados nulos: É possível utilizar o método interpolate() para preencher os valores nulos com valores interpolados, ou seja, valores calculados a partir dos valores vizinhos.