from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    "dagrundag2",
    description="My first dag run dag",
    schedule_interval=None,
    start_date=datetime(2024, 3, 10),
) as dag:
    task_1 = BashOperator(task_id="tsk1", bash_command="sleep 5")
    task_2 = BashOperator(task_id="tsk2", bash_command="sleep 5")

    task_1 >> task_2
