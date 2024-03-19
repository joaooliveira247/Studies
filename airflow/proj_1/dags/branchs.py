from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime
import random


def gen_random_num() -> int:
    return random.randint(1, 100)


def classifier_rand_num(**context):
    print(f"type of context: {type(context)} \n {context}")
    number = context["task_instance"].xcom_pull(task_ids="gen_random_tsk")
    if number % 2 == 0:
        return "even_task"
    return "odd_task"


with DAG(
    "brachs",
    description="branchs example",
    schedule_interval=None,
    start_date=datetime(2024, 3, 13),
    catchup=False,
) as dag:
    gen_random_task = PythonOperator(
        task_id="gen_random_tsk",
        python_callable=gen_random_num,
    )
    branch_task = BranchPythonOperator(
        task_id="branch_task",
        python_callable=classifier_rand_num,
        provide_context=True,
    )
    even_task = BashOperator(task_id="even_task", bash_command="echo 'even'")
    odd_task = BashOperator(task_id="odd_task", bash_command="echo 'odd'")

gen_random_task >> branch_task
branch_task >> even_task
branch_task >> odd_task
