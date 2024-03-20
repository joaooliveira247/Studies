from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.providers.postgres.operators.postgres import PostgresOperator


def show_result(ti) -> None:
    result = ti.xcom_pull(task_ids="read_table")
    print(result)


with DAG(
    "providers",
    description="providers example with databases",
    schedule_interval=None,
    start_date=datetime(2024, 3, 15),
    catchup=False,
) as dag:
    create_table = PostgresOperator(
        task_id="create_table",
        postgres_conn_id="postgres",
        sql="CREATE TABLE IF NOT EXISTS test(id INT);",
    )
    insert_table = PostgresOperator(
        task_id="insert_table",
        postgres_conn_id="postgres",
        sql="INSERT INTO test VALUES(1);",
    )
    read_table = PostgresOperator(
        task_id="read_table",
        postgres_conn_id="postgres",
        sql="SELECT * FROM test;",
    )

    print_result = PythonOperator(
        task_id="print_result",
        python_callable=show_result,
        provide_context=True,
    )

create_table >> insert_table >> read_table >> print_result
