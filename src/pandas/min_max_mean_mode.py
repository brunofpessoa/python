import pandas as pd


df = pd.DataFrame({
  "nome": ["maria", "joão", "joão", "joão", "zeca", "ana"],
  "idade": [13, 12, 35, 23, 76, 23]
})

print(f"name max: {df['nome'].max()}")
print(f"name min: {df['nome'].min()}")
print(f"idade max: {df['idade'].max()}")
print(f"idade max: {df['idade'].min()}")

mean = df["idade"].mean()
median = df["idade"].median()
mode = df["idade"].mode()

print(f"Idade média: {mean}")
print(f"Mediana da idade: {median}")
print(f"Moda da idade: {mode}")
