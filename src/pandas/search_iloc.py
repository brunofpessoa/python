import pandas as pd


data = {
    "comida": ["maçã", "pastel", "coxinha", "doce de leite"],
    "tipo": ["doce", "salgado", "salgado", "doce"]
}

df = pd.DataFrame(data)

last_el = df.iloc[-1]
print(f"iloc search:\n {last_el}")