from airflow import DAG
from airflow.utils.dates import days_ago
from operators.operator_1 import CsvToPydanticOperator


default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

dag = DAG(
    'csv_to_sql_dag',
    default_args=default_args,
    description='A DAG to process CSV and generate SQL',
    schedule_interval=None,
)

process_csv = CsvToPydanticOperator(
    task_id='process_csv',
    csv_path='/opt/airflow/data/input.csv',
    dag=dag,
)
