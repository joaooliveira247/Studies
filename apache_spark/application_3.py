from pyspark.sql import SparkSession
from sys import argv
from getopt import getopt
from pathlib import Path


def main() -> None:
    spark = SparkSession.builder.appName("Exempla Application").getOrCreate()
    opts, _ = getopt(argv[1:], "t:i:o:")
    _format, infile, out_dir = "", "", ""

    for opt, arg in opts:
        match opt:
            case "-t":
                _format = arg
                continue
            case "-i":
                infile = arg
                continue
            case "-o":
                out_dir = arg
                continue
            case _:
                raise Exception("Option not found.")

    data = spark.read.csv(
        str(Path().home().joinpath(infile)),
        header=False,
        inferSchema=True,
    )
    data.write.format(_format).save(str(Path().home().joinpath(out_dir)))


if __name__ == "__main__":
    main()
