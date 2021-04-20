from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'Thomas',
    'depends_on_past': False,
    'email': ['tjmolloy15@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id='MMA',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=7),
    start_date=days_ago(1),
)

task1 = BashOperator(
    task_id='get_mma_data',
    bash_command='python ~/airflow/dags/OpenRoadMediaExampleProject/get_mma_data.py',
    dag=dag
)

task2 = BashOperator(
    task_id='update_mma_db',
    bash_command='python ~/airflow/dags/OpenRoadMediaExampleProject/create_mma_db.py',
    dag=dag
)

task1 >> task2
