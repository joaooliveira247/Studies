from pyspark.sql import SparkSession
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
    opts, _ = getopt(argv[1:], "i:t:")
    infile, table_name = "", ""

    for opt, arg in opts:
        match opt:
            case "-i":
                infile = arg
                continue
            case "-t":
                table_name = arg
                continue
            case _:
                raise Exception("Option not found.")
    load = spark.read.parquet(str(Path().home().joinpath(infile)))
    load.write.format("console").save()
    load.write.format("jdbc").option(
        "url", "jdbc:postgresql://localhost:5432/postgres"
    ).option("dbtable", table_name).option("user", "user").option(
        "password", "passwd"
    ).option("driver", "org.postgresql.Driver").save()


if __name__ == "__main__":
    main()
