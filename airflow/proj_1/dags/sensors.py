from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.http.sensors.http import HttpSensor
from datetime import datetime
from httpx import get


def query_api():
    response = get("https://api.publicapis.org/entries")
    print(response.text)


with DAG(
    "http_sensors",
    description="sensors example",
    schedule_interval=None,
    start_date=datetime(2024, 3, 14),
    catchup=False,
) as dag:
    check_api = HttpSensor(
        task_id="check_api",
        http_conn_id="connection",
        endpoint="entries",
        poke_interval=5,
        timeout=20,
    )
    process_data = PythonOperator(
        task_id="process_data",
        python_callable=query_api,
    )

check_api >> process_data
