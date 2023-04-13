import pandas as pd


def data_frame_exemple():
    print("\n==========DataFrame==========\n")
    df = pd.DataFrame({
        "nome": ["foo", "bar", "baz", "qux"],
        "primeira_nota": [7, 10, 7, 8],
        "segunda_nota": [8, 6, 5, 5]
    })
    df["media"] = (df["primeira_nota"] + df["segunda_nota"]) * 0.5
    df["situacao"] = df["media"].apply(
        lambda media: "Aprovado" if media >= 7 else "Reprovado"
    )

    print(df)


def series_exemple():
    print("\n==========Series==========\n")
    list = ["A", "B", "C"]
    serie = pd.Series(list)

    print(serie)

    dict = {
        "a": "A",
        "b": "B",
        "c": "C",
    }
    serie = pd.Series(dict)

    print(f"\n{serie}")
    print(f"{serie[1]}")
    print(f"{serie['c']}")


def attributes_and_methods_exemple():
    print("\n==========Attributes and methods==========\n")
    df = pd.DataFrame({
        "nome": ["foo", "bar", "baz", "qux"],
        "primeira_nota": [7, 10, 7, 8],
        "segunda_nota": [8, 6, 5, 5]
    })

    print(f"Shape:\n {df.shape}")
    print(f"\nColumns:\n {df.columns}")
    print(f"\nInfo:\n {df.info()}")
    print(f"\nFirst two elements:\n {df.head(2)}")
    print(f"\nLast two elements:\n {df.tail(2)}")
    print(f"\nStatistics:\n {df.describe()}")

    serie = pd.Series(['a', 'b', None, 'c'])
    print("\nisnull/isna:")
    print(serie.isnull().sum())
    print(serie.isna().sum())


def read_csv_exemple():
    print("\n==========read_csv_exemple==========\n")
    path_name = "./exemple.csv"
    df = pd.read_csv(path_name)
    print(df)


def read_json_exemple():
    print("\n==========read_json_exemple==========\n")
    path_name = "./exemple.json"
    df = pd.read_json(path_name)
    print(df)


def to_json_exemple():
    print("\n==========to_json_exemple==========\n")
    path_name = "./to_json_exemple.json"
    data = {
        "Nome": ["Alice", "Bob", "Charlie"],
        "Idade": [25, 30, 35],
        "Cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte"]
    }
    df = pd.DataFrame(data)
    df.to_json(path_or_buf=path_name, orient='records')
    print("arquivo criado em: ./to_json_exemple.json")


def from_csv_to_json_exemple():
    df = pd.read_csv('./exemple.csv')
    df.to_json('./csv_to_json_exemple.json', orient='records')


def loc_exemple():
    print("\n==========loc_exemple==========\n")
    data = {
        "comida": ["abacate", "requeijão", "margarina", "doce de leite"],
        "tipo": ["doce", "salgado", "salgado", "doce"]
    }
    df = pd.DataFrame(data)
    sweet_foods = df.loc[df["tipo"] == "doce"]
    print("loc search:")
    print(sweet_foods)


def iloc_exemple():
    print("\n==========iloc_exemple==========\n")
    data = ["abacate", "requeijão", "margarina"]
    df = pd.DataFrame(data)
    last_el = df.iloc[-1]
    print("iloc search:")
    print(last_el)


def groupby_exemple():
    print("\n==========groupby_exemple==========\n")
    df = pd.read_json("./exemple.json")
    # Agrupa os dados por Cidade e Gênero, e calcula a média da idade por grupo
    average_by_city_gender = df.groupby(['Cidade', 'Gênero'])['Idade'].mean()

    print(average_by_city_gender)


def merge_exemple():
    print("\n==========merge_exemple==========\n")
    primeira_nota = pd.DataFrame({
        "nome": ["maria", "joão", "pedro", "ana"],
        "primeira_nota": [9, 8, 7, 8],
    })

    segunda_nota = pd.DataFrame({
        "nome": ["maria", "joão", "pedro", "ana"],
        "segunda_nota": [8, 7, 9, 3]
    })

    par_de_notas = primeira_nota.merge(segunda_nota)
    print(par_de_notas)


def unique_exemple():
    print("\n==========unique_exemple==========\n")
    df = pd.DataFrame({
        "nome": ["maria", "joão", "joão", "joão", "pedro", "ana"],
    })

    print(df["nome"].unique())


def min_max_exemple():
    print("\n==========unique_exemple==========\n")
    df = pd.DataFrame({
        "nome": ["maria", "joão", "joão", "joão", "zeca", "ana"],
        "idade": [19, 12, 35, 23, 76, 23]
    })

    print(f"name max: {df['nome'].max()}")
    print(f"name min: {df['nome'].min()}")
    print(f"idade max: {df['idade'].max()}")
    print(f"idade max: {df['idade'].min()}")


def mean_median_mode_exemple():
    print("\n==========unique_exemple==========\n")
    serie = pd.Series([2, 2, 3, 4, 5])

    print(f"Average: {serie.mean()}")
    print(f"Median: {serie.median()}")
    print(f"Mode: {serie.mode()}")


if __name__ == "__main__":
    data_frame_exemple()
    series_exemple()
    attributes_and_methods_exemple()
    read_csv_exemple()
    read_json_exemple()
    to_json_exemple()
    from_csv_to_json_exemple()
    loc_exemple()
    iloc_exemple()
    groupby_exemple()
    merge_exemple()
    unique_exemple()
    min_max_exemple()
    mean_median_mode_exemple()
