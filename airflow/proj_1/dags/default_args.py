from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args: dict = {
    "depends_on_past": False,
    "start_date": datetime(2024, 3, 12),
    "email": ["test@test.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(seconds=10),
}


with DAG(
    "default_args_dag",
    description="default args dag",
    default_args=default_args,
    schedule_interval="@hourly",
    start_date=datetime(2024, 3, 12),
    catchup=False,
    default_view="graph",
    tags=["process", "tag", "pipeline"],
) as dag:
    task_1 = BashOperator(
        task_id="tsk1",
        bash_command="sleep 5",
        retries=3,
    )
    task_2 = BashOperator(
        task_id="tsk2",
        bash_command="sleep 5",
    )
    task_3 = BashOperator(
        task_id="tsk3",
        bash_command="sleep 5",
    )

    task_1 >> task_2 >> task_3
