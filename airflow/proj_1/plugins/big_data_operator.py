from typing import Any
from airflow.models import BaseOperator
from airflow.utils.context import Context
from airflow.utils.decorators import apply_defaults
import pandas as pd


class BigDataOperator(BaseOperator):
    @apply_defaults
    def __init__(
        self,
        path_to_csv_file: str,
        path_to_output_file: str,
        sep: str = ";",
        file_type: str = "parquet",
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)
        self.path_to_csv_file = path_to_csv_file
        self.path_to_output_file = path_to_output_file
        self.sep = sep
        self.file_type = file_type

    def execute(self, context: Context) -> Any:
        df = pd.read_csv(self.path_to_csv_file, sep=self.sep)
        if self.file_type == "parquet":
            df.to_parquet(self.path_to_output_file)
            return
        elif self.file_type == "json":
            df.to_json(self.path_to_output_file)
            return
        else:
            raise ValueError("Invalid value to path_to_output_file")
