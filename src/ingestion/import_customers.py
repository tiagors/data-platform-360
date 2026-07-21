import pandas as pd
import time
import logging
from datetime import datetime
from pathlib import Path

from src.utils.database import get_connection
from src.utils.paths import DATASETS_DIR
from src.utils.paths import LOGS_DIR



log_file = LOGS_DIR / f"pipeline_{datetime.now():%Y-%m-%d}.log"

logger = logging.getLogger("pipeline")

if not logger.handlers:
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)-8s | %(message)s"
    )

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    file_handler = logging.FileHandler(
        log_file,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file_handler)


def import_customers():

    inicio = time.perf_counter()

    conn = None
    cursor = None 

    try:

        csv_path = DATASETS_DIR / "customers.csv"

        df = pd.read_csv(csv_path)
        logger.info(f"Registros encontrados: {len(df)}")

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
        logger.info(f"Tempo: {tempo_execucao:.2f} segundos")

        logger.info("=" * 60)
        logger.info("Pipeline finalizado")
        logger.info(f"Arquivo..............: {csv_path.name}")
        logger.info(f"Registros lidos......: {registros_lidos}")
        logger.info(f"Registros processados: {registros_processados}")
        logger.info(f"Registros inseridos..: {registros_inseridos}")
        logger.info(f"Registros ignorados..: {registros_ignorados}")
        logger.info(f"Tempo total..........: {tempo_execucao:.2f} s")
        logger.info("=" * 60)

    except Exception as e:

        if conn is not None:
            conn.rollback()

        logger.error("=" * 60)
        logger.error("Pipeline finalizado com erro")
        logger.error(f"Erro: {e}")
        logger.exception("Erro durante execução do pipeline.")
        logger.error("=" * 60)

    finally:
        
        if cursor is not None: 
            cursor.close()

        if conn is not None:
            conn.close()

    

if __name__ == "__main__":
    import_customers()