from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.email import EmailOperator
from airflow.sensors.filesystem import FileSensor
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.models import Variable
from airflow.utils.task_group import TaskGroup
from datetime import datetime, timedelta
import json
import os

default_args: dict = {
    "depends_on_past": False,
    "email": ["email@email.com"],
    "email_on_failure": True,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(seconds=10),
    "default_view": "graph",
}


def process_file(**kwargs):
    with open(Variable.get("path_file")) as f:
        data = json.load(f)
        kwargs["ti"].xcom_push(key="idtemp", value=data["idtemp"])
        kwargs["ti"].xcom_push(key="powerfactor", value=data["powerfactor"])
        kwargs["ti"].xcom_push(
            key="hydraulicpressure",
            value=data["hydraulicpressure"],
        )
        kwargs["ti"].xcom_push(key="temperature", value=data["temperature"])
        kwargs["ti"].xcom_push(key="timestamp", value=data["timestamp"])
        os.remove(Variable.get("file_path"))


def temp_check(**context):
    number = float(context["ti"].xcom_pull(task_ids="get_data", key="temperature"))
    if number >= 24:
        return "group_check_temp.send_email_alert"
    return "group_check_temp.send_email_alert"


with DAG(
    "wind_turbine",
    description="end project",
    default_args=default_args,
    schedule_interval=None,
    start_date=datetime(2024, 3, 16),
    tags=["wind tubine", "pipeline"],
    doc_md="## Dag to register some data from wind turbine",
) as dag:
    group_check_temp = TaskGroup("check_temp_group")
    group_database = TaskGroup("database_group")
    file_sensor_task = FileSensor(
        task_id="file_sensor",
        filepath=Variable.get("path_file"),
        fs_conn_id="fs_default",
        poke_interval=10,
    )
    get_data_task = PythonOperator(
        task_id="get_data", python_callable=process_file, provide_context=True
    )
    create_table = PostgresOperator(
        task_id="create_table",
        postgres_conn_id="postgres",
        sql="""
            CREATE TABLE IF NOT EXISTS sensors(
                idtemp VARCHAR, powerfactor VARCHAR, hydraulicpressure VARCHAR,
                temperature VARCHAR, timestamp VARCHAR
                );
            """,
        task_group=group_database,
    )
    insert_data = PostgresOperator(
        task_id="insert_data",
        postgres_conn_id="postgres",
        parameters=(
            '{{ ti.xcom_pull(task_ids="get_data", key="idtemp") }}',
            '{{ ti.xcom_pull(task_ids="get_data", key="powerfactor") }}',
            '{{ ti.xcom_pull(task_ids="get_data", key="hydraulicpressure") }}',
            '{{ ti.xcom_pull(task_ids="get_data", key="temperature") }}',
            '{{ ti.xcom_pull(task_ids="get_data", key="timestamp") }}',
        ),
        sql="""
            INSERT INTO sensors(
                idtemp, powerfactor, hydraulicpressure, temperature, timestamp
                ) VALUES (%s, %s, %s, %s, %s);
        """,
        task_group=group_database,
    )
    send_email_alert = EmailOperator(
        task_id="send_email_alert",
        to="email@email.com",
        sunject="Airflow Alert",
        html_content="<h3>Alert</h3>",
        task_group=group_check_temp,
    )
    send_email = EmailOperator(
        task_id="send_email",
        to="email@email.com",
        sunject="Airflow Email",
        html_content="<h3>Normal</h3>",
        task_group=group_check_temp,
    )
    check_temp_branch = BranchPythonOperator(
        task_id="check_temp_branch",
        python_callable=temp_check,
        provide_context=True,
        task_group=group_check_temp,
    )

with group_check_temp:
    check_temp_branch >> [send_email_alert, send_email]

with group_database:
    create_table >> insert_data

file_sensor_task >> get_data_task
get_data_task >> group_check_temp
get_data_task >> group_database
