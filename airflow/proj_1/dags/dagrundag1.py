from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.operators.trigger_dagrun import TriggerDagRunOperator


with DAG(
    "dagrundag1",
    description="My first dag run dag",
    schedule_interval=None,
    start_date=datetime(2024, 3, 10),
) as dag:
    task_1 = BashOperator(task_id="tsk1", bash_command="sleep 5")
    task_2 = TriggerDagRunOperator(task_id="tsk2", trigger_dag_id="dagrundag2")

    task_1 >> task_2
