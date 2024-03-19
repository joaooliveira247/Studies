from airflow import DAG
from airflow.datasets import Dataset
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd


my_dataset = Dataset("/opt/airflow/data/Churn_new.csv")


def my_file():
    dataset = pd.read_csv("/opt/airflow/data/Churn_new.csv", sep=";")
    dataset.to_csv("/opt/airflow/data/Churn_new2.csv")


with DAG(
    "consumer",
    description="DAG dataset",
    schedule=[my_dataset],
    start_date=datetime(2024, 3, 14),
    tags=["data", "pipeline", "pandas", "data-cleaning", "dataset"],
) as dag:
    task_1 = PythonOperator(
        task_id="tsk1", python_callable=my_file, provide_context=True
    )

task_1
