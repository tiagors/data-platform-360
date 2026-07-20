from pathlib import Path

import pandas as pd

csv_path = Path("datasets/customers.csv")

df = pd.read_csv(csv_path)

print("=== Primeiras linhas ===")
print(df.head())

print("\n=== Informações ===")
df.info()

print("\n=== Quantidade de linhas ===")
print(len(df))

print("\n=== Quantidade de colunas ===")
print(len(df.columns))

print("\n=== Shape ===")
print(df.shape)

print("\n=== Tipos ===")
print(df.dtypes)