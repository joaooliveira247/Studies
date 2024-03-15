from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

dag = DAG(
    "second_dag",
    description="My second DAG",
    schedule_interval=None,
    start_date=datetime(2024, 3, 10),
    catchup=False,  # if cathup airflow will execute passed dates diffente now
)

task_1 = BashOperator(task_id="tsk1", bash_command="sleep 5", dag=dag)
task_2 = BashOperator(task_id="tsk2", bash_command="sleep 5", dag=dag)
task_3 = BashOperator(task_id="tsk3", bash_command="sleep 5", dag=dag)

# operation task_2, task_3 in pararel
task_1 >> [task_2, task_3]