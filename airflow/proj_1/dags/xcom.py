from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def task_write(**kwargs):
    kwargs["ti"].xcom_push(key="xcomvalue1", value=10200)


def task_read(**kwargs) -> None:
    value = kwargs["ti"].xcom_pull(key="xcomvalue1")
    print(f"value catch from {'xcomvalue1'}: {value}")


with DAG(
    "xcom",
    description="using xcom",
    schedule_interval=None,
    start_date=datetime(2024, 3, 12),
    catchup=False,
) as dag:
    ...
    task_1 = PythonOperator(task_id="tsk1", python_callable=task_write)
    task_2 = PythonOperator(task_id="tsk2", python_callable=task_read)

    task_1 >> task_2
