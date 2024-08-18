import time
from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2024, 8, 18),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "simple_dag",
    default_args=default_args,
    description="A simple DAG",
    schedule_interval=timedelta(days=1),
)


def print_current_time():
    now = datetime.now()
    print(f"現在の日時: {now}")


def perform_calculation():
    result = 2 + 2
    print(f"2 + 2 = {result}")
    time.sleep(5)  # 5秒間スリープして処理時間をシミュレート


def print_message():
    print("DAGの実行が完了しました！")


t1 = PythonOperator(
    task_id="print_current_time",
    python_callable=print_current_time,
    dag=dag,
)

t2 = PythonOperator(
    task_id="perform_calculation",
    python_callable=perform_calculation,
    dag=dag,
)

t3 = PythonOperator(
    task_id="print_message",
    python_callable=print_message,
    dag=dag,
)

t1 >> t2 >> t3
