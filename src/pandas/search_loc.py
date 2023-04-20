import pandas as pd


data = {
    "comida": ["maçã", "pastel", "coxinha", "doce de leite"],
    "tipo": ["doce", "salgado", "salgado", "doce"]
}

df = pd.DataFrame(data)

sweet_foods = df.loc[df["tipo"] == "doce"]

print(f"Doces:\n {sweet_foods}")
