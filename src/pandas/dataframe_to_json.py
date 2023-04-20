import pandas as pd


data = {
    "Nome": ["Alice", "Bob", "Charlie"],
    "Idade": [25, 30, 35],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
}

df = pd.DataFrame(data)

path_name = "src/pandas/files/dataframe_to_json.json"
df.to_json(path_or_buf=path_name, orient='records')

print("Criado em: src/pandas/files/dataframe_to_json.json")
