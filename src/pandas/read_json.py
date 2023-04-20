import pandas as pd


path_name = "src/pandas/files/exemple.json"
df = pd.read_json(path_name)
print(df)