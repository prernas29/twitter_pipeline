from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from twitter_etl import modify_and_save_csv_from_api

default_args = {
    'owner': 'airflow',
}

# Define the start date as now
start_date = datetime.now()

dag = DAG(
    'twitter_dag',
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule_interval=timedelta(hours=1),  # Run the DAG every hour
    start_date=start_date,  # Start the DAG now
)

run_etl = PythonOperator(
    task_id='complete_twitter_etl',
    python_callable=modify_and_save_csv_from_api,
    dag=dag,
)

run_etl
