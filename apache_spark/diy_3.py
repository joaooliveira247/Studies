from pyspark.sql import SparkSession, DataFrame
from pyspark.sql import functions as func
from pathlib import Path
from sys import argv
from getopt import getopt

BASE_DIR = Path().home() / "Documents/PySparkCurso/download"


def main() -> None:
    spark = (
        SparkSession.builder.master("local")
        .config("spark.jars", str(BASE_DIR / "postgresql-42.7.3.jar"))
        .appName("Do It Youself - Three")
        .getOrCreate()
    )


if __name__ == "__main__":
    main()
