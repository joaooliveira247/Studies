from airflow import DAG
from datetime import datetime
from big_data_operator import BigDataOperator


with DAG(
    "big_data",
    description="A simple plugin",
    schedule_interval=None,
    start_date=datetime(2024, 3, 15),
    tags=["plugin"],
) as dag:
    big_data = BigDataOperator(
        task_id="big_data",
        path_to_csv_file="/opt/airflow/data/Churn.csv",
        path_to_output_file="/opt/airflow/data/Churn.json",
        file_type="json",
        sep=";",
    )

big_data
