import pandas as pd


df = pd.DataFrame({
    "nome": ["Ana", "João", "Francisco", "José"],
    "primeira_nota": [7, 10, 7, 8],
    "segunda_nota": [8, 6, 5, 5]
})
df["media"] = (df["primeira_nota"] + df["segunda_nota"]) * 0.5
df["situacao"] = df["media"].apply(
    lambda media: "Aprovado" if media >= 7 else "Reprovado"
)

print(df)

nome_e_situacao = df[['nome', 'situacao']]
print(f"\nSelecionando apenas nome e situação:\n {nome_e_situacao}")