from airflow.models import BaseOperator
from airflow.utils.decorators import apply_defaults
from typing import List
from csv_to_sql.Loaders.csv import parse_csv
from csv_to_sql.models.basic_settings import BasicSettings

class CsvToPydanticOperator(BaseOperator):
    @apply_defaults
    def __init__(self, csv_path: str, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.csv_path = csv_path

    def execute(self, context):
        data: List[BasicSettings] = parse_csv(self.csv_path)
        context['ti'].xcom_push(key='parsed_data', value=[model.model_dump() for model in data])
        return f"Processed {len(data)} records"
