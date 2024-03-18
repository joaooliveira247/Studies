from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from datetime import datetime, timedelta

default_args: dict = {
    "depends_on_past": False,
    "start_date": datetime(2024, 3, 13),
    "email": ["email@email.com"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(seconds=10),
}


with DAG(
    "email_test",
    description="email test dag",
    default_args=default_args,
    schedule_interval="None",
    catchup=False,
    default_view="graph",
    tags=["process", "tag", "pipeline", "email"],
) as dag:
    task_1 = BashOperator(
        task_id="tsk1",
        bash_command="sleep 1",
    )
    task_2 = BashOperator(
        task_id="tsk2",
        bash_command="sleep 1",
    )
    task_3 = BashOperator(
        task_id="tsk3",
        bash_command="exit 1",
    )
    task_4 = BashOperator(
        task_id="tsk4",
        bash_command="sleep 1",
    )
    task_5 = BashOperator(
        task_id="tsk5", bash_command="sleep 1", trigger_rule="none_failed"
    )
    task_6 = BashOperator(
        task_id="tsk6", bash_command="sleep 1", trigger_rule="none_failed"
    )
    send_email = EmailOperator(
        task_id="send_email",
        to="your_email",
        subject="Airflow Error",
        html_content="<h3>Dag's Error</h3>",
        trigger_rule="one_failed",
    )

    [task_1, task_2] >> task_3 >> task_4
    task_4 >> [send_email, task_5, task_6]
