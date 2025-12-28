from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.sensors.filesystem import FileSensor
from datetime import datetime, timedelta
import os

# Define default arguments
default_args = {
    'owner': 'acdba_dev_ref',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

# Define the DAG
with DAG(
    '00_test_sensor_dag',        # The unique ID of the DAG
    default_args=default_args,
    description='A simple test DAG with a Sensor',
    schedule_interval=None,      # None means manual trigger only
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    # Task 1: Wait for a file to appear in /tmp
    wait_for_file = FileSensor(
        task_id='wait_for_trigger_file',
        filepath='/tmp/airflow_test_trigger',
        poke_interval=10,        # Check every 10 seconds
        timeout=600,             # Fail after 10 minutes
        mode='poke'              # 'poke' keeps the worker slot occupied (good for testing)
    )

    # Task 2: Run a Python function
    def print_success():
        print("File found! The sensor worked and the DAG is complete.")
        # Optional: Clean up the trigger file so we can test again later
        if os.path.exists('/tmp/airflow_test_trigger'):
            os.remove('/tmp/airflow_test_trigger')
            print("Trigger file removed.")

    process_file = PythonOperator(
        task_id='process_file',
        python_callable=print_success
    )

    # Define Dependency
    wait_for_file >> process_file
