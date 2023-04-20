import pandas as pd


df = pd.DataFrame({
  "nome": ["maria", "joão", "joão", "joão", "pedro", "ana"],
})

print(df["nome"].unique())