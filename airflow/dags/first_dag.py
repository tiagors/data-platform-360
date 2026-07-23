from datetime import datetime

from airflow import DAG
from airflow.operators.empty import EmptyOperator


with DAG(
    dag_id="first_dag",
    description="Primeira DAG da Data Platform 360",
    start_date=datetime(2026, 1, 1),
    schedule=None,          # Execução somente manual
    catchup=False,
    tags=["learning", "data-platform-360"],
) as dag:

    start = EmptyOperator(
        task_id="start"
    )

    validate_environment = EmptyOperator(
        task_id="validate_environment"
    )

    finish = EmptyOperator(
        task_id="finish"
    )

    start >> validate_environment >> finish