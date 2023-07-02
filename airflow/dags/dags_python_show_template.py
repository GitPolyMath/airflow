from airflow import DAG
import pendulum
import datetime
from airflow.decorators import task
from airflow.operators.python import PythonOperator



with DAG(
    dag_id = "dags_python_show_template" ,
    schedule = "30 9 * * *",
    start_date = pendulum.datetime(2023, 6, 27, tz = "Asia/Seoul"),
    catchup = True
) as dag:
    
    @task(task_id = 'python_task_1')
    def show_templates(**kwargs):
        from pprint import pprint
        pprint(kwargs)

    show_templates()
