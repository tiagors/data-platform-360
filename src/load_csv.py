import pandas as pd

from utils.paths import CUSTOMERS_CSV

df = pd.read_csv(CUSTOMERS_CSV)

print("=" * 50)
print("Informações do DataFrame")
print("=" * 50)
print(df.info())

print("\nPrimeiras linhas")
print(df.head())

linhas, colunas = df.shape

print(f"\nQuantidade de linhas: {linhas}")
print(f"Quantidade de colunas: {colunas}")
