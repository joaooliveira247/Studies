from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.models import Variable


def my_print(**context) -> None:
    my_var = Variable.get("my_var")
    print(f"my_print: {my_var}")


with DAG(
    "var_example",
    description="var example",
    schedule_interval=None,
    start_date=datetime(2024, 3, 13),
    catchup=False,
) as dag:
    task_1 = PythonOperator(
        task_id="tsk1",
        python_callable=my_print,
    )

task_1
