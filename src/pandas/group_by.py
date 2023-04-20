import pandas as pd


data = {
    "Nome": ["Ana", "Bruno", "Carla", "Diego", "Elaine", "Fernando", "Gabriela", "Helena"],
    "Gênero": ["F", "M", "M", "F", "F", "M", "F", "F"],
    "Idade": [25, 35, 18, 22, 27, 31, 24, 29],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "São Paulo", "Rio de Janeiro", "Belo Horizonte", "São Paulo", "Rio de Janeiro"]
}

df = pd.DataFrame(data)

# Agrupa por Cidade e Gênero
# e calcula a média da idade por grupo
average_by_city_gender = df.groupby(['Cidade', 'Gênero'])['Idade'].mean()

print(average_by_city_gender)