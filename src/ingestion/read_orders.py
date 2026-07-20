from pathlib import Path

import pandas as pd

csv_path = Path("datasets/orders.csv")

df = pd.read_csv(csv_path)

print("=== Primeiras linhas ===")
print(df.head())

print("\n=== Últimas linhas ===")
print(df.tail())

print("\n=== Informações ===")
df.info()

print("\n=== Shape ===")
print(df.shape)

print("\n=== Quantidade de linhas ===")
print(len(df))

print("\n=== Quantidade de colunas ===")
print(len(df.columns))

print("\n=== Nome das colunas ===")
print(df.columns.tolist())

print("\n=== Tipos das colunas ===")
print(df.dtypes)

print("\n=== Valores nulos por coluna ===")
print(df.isnull().sum())

print("\n=== Linhas com algum valor nulo ===")
print(df.isnull().any(axis=1).sum())

print("\n=== Dados duplicados ===")
print(df.duplicated().sum())

print("\n=== Última linha ===")
print(df.tail(1))