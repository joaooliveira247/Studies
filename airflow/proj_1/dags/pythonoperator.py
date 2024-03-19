from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd
import statistics as sts


def data_cleaning():
    dataset = pd.read_csv("/opt/airflow/data/Churn.csv", sep=";")
    dataset.columns = [
        "id",
        "score",
        "estado",
        "genero",
        "idade",
        "patrimonio",
        "saldo",
        "produtos",
        "temcardcredito",
        "ativo",
        "salario",
        "saiu",
    ]
    pay_median = sts.median(dataset["salario"])
    dataset["salario"].fillna(pay_median, inplace=True)

    dataset["genero"].fillna("null", inplace=True)

    age_median = sts.median(dataset["idade"])
    dataset.loc[(dataset["idade"] < 0) | (dataset["idade"] > 120), "idade"] = age_median
    dataset.drop_duplicates(subset="id", keep="first", inplace=True)

    dataset.to_csv("/opt/airflow/data/Churn_cleaned.csv", sep=";", index=False)


with DAG(
    "python_operator",
    description="Python Operator simple example pipeline",
    schedule_interval=None,
    start_date=datetime(2024, 3, 14),
    tags=["data", "pipeline", "pandas", "data-cleaning"],
) as dag:
    data_clean = PythonOperator(
        task_id="data_clean",
        python_callable=data_cleaning,
    )


data_clean
