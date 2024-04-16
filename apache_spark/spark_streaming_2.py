from pyspark.sql import SparkSession, DataFrame
from pathlib import Path


def att_postgres(df: DataFrame, batch_id: int):
    df.write.format("jdbc").option(
        "url", "jdbc:postgresql://localhost:5432/postgres"
    ).option("dbtable", "posts").option("user", "user").option(
        "password", "passwd"
    ).option("driver", "org.postgresql.Driver").mode("append").save()


if __name__ == "__main__":
    BASE_DATA_DIR = Path().home() / "Documents/PySparkCurso/download"

    spark: SparkSession = (
        SparkSession.builder.master("local")
        .appName("streaming with spark saving postgres")
        .getOrCreate()
    )

    json_schema = "nome STRING, postagem STRING, data INT"

    df = spark.readStream.json(
        str(BASE_DATA_DIR / "test_streaming/"), schema=json_schema
    )

    temp_dir = BASE_DATA_DIR / "temp/"

    stcal = (
        df.writeStream.foreachBatch(att_postgres)
        .outputMode("append")
        .trigger(processingTime="5 seconds")
        .option("checkpointlocation", temp_dir)
        .start()
    )
    stcal.awaitTermination()
