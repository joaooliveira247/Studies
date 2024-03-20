from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime
from enum import Enum


class QueryType(Enum):
    run = 1
    get_records = 2


def query(query: str, query_type: QueryType) -> None:
    pg_hook = PostgresHook(postgres_conn_id="postgres")
    if query_type == QueryType.run:
        pg_hook.run(query, autocommit=True)
        return
    if QueryType.get_records:
        return pg_hook.get_records(query)


def create_table(table_name: str, fields: str) -> None:
    query(
        f"CREATE TABLE IF NOT EXISTS {table_name}({fields});",
        QueryType.run,
    )


def insert_data(table_name: str, values: str) -> None:
    query(
        f"INSERT INTO {table_name} VALUES({values});",
        QueryType.run,
    )


def select_data(table_name: str, **kwargs) -> None:
    records = query(f"SELECT * FROM {table_name};", QueryType.get_records)
    print(records)
    kwargs["ti"].xcom_push(key="query_result", value=records)


def print_data(ti) -> None:
    task_instace = ti.xcom_pull(
        key="query_result",
        task_ids="select_data_task",
    )
    print(ti)
    print(f"Data from table:\n {task_instace}")


with DAG(
    "hooks",
    description="example hooks",
    schedule_interval=None,
    start_date=datetime(2024, 3, 15),
    catchup=False,
    default_view="graph",
) as dag:
    create_table_task = PythonOperator(
        task_id="create_table_task",
        python_callable=create_table,
        op_kwargs={"table_name": "teste2", "fields": "id INT"},
    )
    insert_data_task = PythonOperator(
        task_id="insert_table_task",
        python_callable=insert_data,
        op_kwargs={"table_name": "teste2", "values": "1"},
    )
    select_data_task = PythonOperator(
        task_id="select_table_task",
        python_callable=select_data,
        op_kwargs={"table_name": "teste2"},
        provide_context=True,
    )
    print_data_task = PythonOperator(
        task_id="print_table_task",
        python_callable=print_data,
        provide_context=True,
    )

create_table_task >> insert_data_task >> select_data_task >> print_data_task
