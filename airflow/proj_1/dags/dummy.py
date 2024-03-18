from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    "dummy_dag",
    description="tasks dummy",
    schedule_interval=None,
    start_date=datetime(2024, 3, 13),
    catchup=False,
) as dag:
    task_1 = BashOperator(task_id="tsk1", bash_command="sleep 1")
    task_2 = BashOperator(task_id="tsk2", bash_command="sleep 1")
    task_3 = BashOperator(task_id="tsk3", bash_command="sleep 1")
    task_4 = BashOperator(task_id="tsk4", bash_command="sleep 1")
    task_5 = BashOperator(task_id="tsk5", bash_command="sleep 1")
    # replacement of dummy operator
    empty_task = EmptyOperator(task_id="task_dummy")


[task_1, task_2, task_3] >> empty_task >> [task_4, task_5]
