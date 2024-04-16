from pathlib import Path
from pyspark.sql import SparkSession


if __name__ == "__main__":
    BASE_DATA_DIR = Path().home() / "Documents/PySparkCurso/download"

    spark: SparkSession = (
        SparkSession.builder.master("local")
        .appName("streaming with spark")
        .getOrCreate()
    )
    json_schema = "nome STRING, postagem STRING, data STRING"
    df = spark.readStream.json(
        str(BASE_DATA_DIR / "test_streaming/"),
        schema=json_schema,
    )

    TEMP_DIR = BASE_DATA_DIR / "temp"

    stcal = (
        df.writeStream.format("console")
        .outputMode("append")
        .trigger(processingTime="5 seconds")
        .option("checkpointlocation", TEMP_DIR)
        .start()
    )

    stcal.awaitTermination()
