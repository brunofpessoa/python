import pandas as pd


df = pd.DataFrame({
    "nome": ["Ana", "João", "Francisco", "José"],
    "primeira_nota": [7, 10, 7, 8],
    "segunda_nota": [8, 6, 5, 5]
})

print(f"Shape: {df.shape}")
print(f"\nColumns:\n {df.columns}")
print(f"\nInfo:\n {df.info}")
print(f"\nFirst two elements:\n {df.head(2)}")
print(f"\nLast two elements:\n {df.tail(2)}")
print(f"\nStatistics:\n {df.describe()}")

serie = pd.Series(['a', 'b', None, 'c'])
print("\nisnull/isna:")
print(serie.isnull().sum())
print(serie.isna().sum())