from pyspark.sql import SparkSession
from pyspark.sql import functions as func
from sys import argv


def main() -> None:
    spark = SparkSession.builder.appName("Exempla Application").getOrCreate()
    arq_schema = "id INT, name STRING, status STRING, city STRING, sales INT, date DATE"
    despachantes = spark.read.csv(argv[1], schema=arq_schema, header=False)

    calc = despachantes.select("date").groupBy(func.year("date")).count()
    calc.write.format("console").save()
    spark.stop()


if __name__ == "__main__":
    main()
