from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from pathlib import Path

BASE_ARQ_DIR = Path().home() / "Documents/PySparkCurso/download"


def main() -> None:
    spark = SparkSession.builder.appName("Exempla Application").getOrCreate()
    arq_schema = "id INT, name STRING, status STRING, city STRING, sales INT, date DATE"
    despachantes = spark.read.csv(
        str(BASE_ARQ_DIR / "despachantes.csv"), schema=arq_schema, header=False
    )

    calc = despachantes.select("date").groupBy(func.year("date")).count()
    calc.write.format("console").save()
    spark.stop()


if __name__ == "__main__":
    main()
