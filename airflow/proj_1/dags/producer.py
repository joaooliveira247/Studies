from airflow import DAG
from airflow.datasets import Dataset
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd


def my_file():
    dataset = pd.read_csv("/opt/airflow/data/Churn.csv", sep=";")
    dataset.to_csv("/opt/airflow/data/Churn_new.csv")


with DAG(
    "producer",
    description="DAG dataset example",
    schedule_interval=None,
    start_date=datetime(2024, 3, 14),
    tags=["data", "pipeline", "pandas", "data-cleaning", "dataset"],
) as dag:
    my_dataset = Dataset("/opt/airflow/data/Churn_new.csv")

    task_1 = PythonOperator(
        task_id="tsk1", python_callable=my_file, outlets=[my_dataset]
    )

task_1
