from pathlib import Path

import pandas as pd

csv_path = Path("datasets/customers.csv")

df = pd.read_csv(csv_path)

# Seleção de colunas
df = df[
    [
        "customer_id",
        "first_name",
        "last_name",
        "email",
        "created_at",
    ]
]

# Limpeza
df["first_name"] = df["first_name"].str.strip()
df["last_name"] = df["last_name"].str.strip()
df["email"] = df["email"].str.strip().str.lower()

# Transformação
df["full_name"] = df["first_name"] + " " + df["last_name"]

# Tipos
df["customer_id"] = df["customer_id"].astype(int)

# Validação de registros inválidos
invalidos = df[
    (df["customer_id"].isna()) |
    (df["first_name"].isna()) | (df["first_name"].str.strip() == "") |
    (df["last_name"].isna())  | (df["last_name"].str.strip() == "") |
    (df["email"].isna())      | (df["email"].str.strip() == "")
]

# Validação de e-mails duplicados
emails_duplicados = df[df.duplicated(subset=["email"], keep=False)]

print("=== Dados transformados ===")
print(df.head())

print("\n=== Registros inválidos ===")
print(invalidos)

print("\n=== E-mails duplicados ===")
print(emails_duplicados)

print(f"\nTotal de e-mails duplicados: {emails_duplicados['email'].nunique()}")