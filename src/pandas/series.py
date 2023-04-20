import pandas as pd


python_list = ["A", "B", "C"]
serie = pd.Series(python_list)

print(serie)

dict = {
    "a": "A",
    "b": "B",
    "c": "C",
}
serie = pd.Series(dict)

# Acessando os elementos
print(f"{serie}")
print(f"{serie[1]}")
print(f"{serie['c']}")