from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    "second_trigger_dag",
    description="My second trigger DAG",
    schedule_interval=None,
    start_date=datetime(2023, 3, 5),
    catchup=False,
) as dag:
    task_1 = BashOperator(task_id="tsk1", bash_command="exit 1")
    task_2 = BashOperator(task_id="tsk2", bash_command="sleep 5")
    task_3 = BashOperator(
        task_id="tsk3", bash_command="sleep 5", trigger_rule="one_failed"
    )

    [task_1, task_2] >> task_3
