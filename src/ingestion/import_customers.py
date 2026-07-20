import pandas as pd
import time

from src.utils.database import get_connection
from src.utils.paths import DATASETS_DIR

inicio = time.perf_counter()

def import_customers():

    conn = None
    cursor = None 

    try:

        csv_path = DATASETS_DIR / "customers.csv"

        df = pd.read_csv(csv_path)

        registros_lidos = len(df)
        registros_processados = 0
        registros_inseridos = 0
        registros_ignorados = 0

        conn = None
        cursor = None 

        conn = get_connection()
        cursor = conn.cursor()

        for _, row in df.iterrows():

            cursor.execute(
                """
                INSERT INTO customers (
                    customer_id,
                    first_name,
                    last_name,
                    email,
                    created_at
                )
                VALUES (%s, %s, %s, %s, %s)
                ON CONFLICT (customer_id) DO NOTHING
                """,
                (
                    row["customer_id"],
                    row["first_name"],
                    row["last_name"],
                    row["email"],
                    row["created_at"],
                ),
            )
            registros_processados += 1

            if cursor.rowcount == 1:
                registros_inseridos += 1
            else:
                registros_ignorados += 1

        conn.commit()

        fim = time.perf_counter()
        tempo_execucao = fim - inicio

        print("\n========================================")
        print("Pipeline finalizado")
        print("========================================")
        print(f"Arquivo: {csv_path.name}")
        print(f"Registros lidos: {registros_lidos}")
        print(f"Registros processados: {registros_processados}")
        print(f"Registros inseridos: {registros_inseridos}")
        print(f"Registros ignorados: {registros_ignorados}")
        print(f"Tempo de execução.....: {tempo_execucao:.2f} s")

    except Exception as e:

        if conn is not None:
            conn.rollback()

        print("\n========================================")
        print("Pipeline finalizado com erro")
        print("========================================")
        print(f"Erro: {e}")

    finally:
        
        if cursor is not None: 
            cursor.close()

        if conn is not None:
            conn.close()

    

if __name__ == "__main__":
    import_customers()