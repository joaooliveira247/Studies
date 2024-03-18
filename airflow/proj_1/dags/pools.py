from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime


with DAG(
    "pools_example",
    description="pools example",
    schedule_interval=None,
    start_date=datetime(2024, 3, 13),
    catchup=False,
) as dag:
    task_1 = BashOperator(
        task_id="tsk1",
        bash_command="sleep 5",
        pool="my_pool",
    )
    task_2 = BashOperator(
        task_id="tsk2",
        bash_command="sleep 5",
        pool="my_pool",
        priority_weight=5,
    )
    task_3 = BashOperator(
        task_id="tsk3",
        bash_command="sleep 5",
        pool="my_pool",
    )
    task_4 = BashOperator(
        task_id="tsk4",
        bash_command="sleep 5",
        pool="my_pool",
        priority_weight=10,
    )
