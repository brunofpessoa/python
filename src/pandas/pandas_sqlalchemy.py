import pandas as pd
from sqlalchemy import create_engine

# Configurações da conexão com o banco de dados
username = 'seu_usuario'
password = 'sua_senha'
host = 'localhost'
database_name = 'nome_do_banco'

# Criando a conexão com o banco de dados mysql
engine = create_engine(
    f'mysql+pymysql://{username}:{password}@{host}/{database_name}'
)

# Criando um DataFrame de exemplo
dados = {
    'nome': ['João', 'Maria', 'Pedro'],
    'idade': [25, 30, 35]
}

df = pd.DataFrame(dados)

# Inserindo os dados do DataFrame em uma tabela do MySQL usando o método to_sql
nome_tabela = 'pessoas'
df.to_sql(name=nome_tabela, con=engine, if_exists='replace', index=False)

# Lendo os dados da tabela e exibindo-os
consulta = f"SELECT * FROM {nome_tabela}"
df_lido = pd.read_sql_query(consulta, con=engine)
print(df_lido)
