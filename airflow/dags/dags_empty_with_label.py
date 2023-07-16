from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.utils.task_group import TaskGroup
from airflow.utils.edgemodifier import Label

import pendulum

with DAG(
    dag_id = "dags_empty_with_label" ,
    schedule = "10 0 * * *",
    start_date = pendulum.datetime(2023, 7, 1, tz = "Asia/Seoul"),
    catchup = False
) as dag:
    
    empty_1 = EmptyOperator(
        task_id = 'empty_1'
    )

    empty_2 = EmptyOperator(
        task_id = 'empty_2'
    )

    empty_1 >> Label('1과 2 사이') >> empty_2

    empty_3 = EmptyOperator(
        task_id = 'empty_3'
    )

    empty_4 = EmptyOperator(
        task_id = 'empty_4'
    )

    empty_5 = EmptyOperator(
        task_id = 'empty_5'
    )

    empty_6 = EmptyOperator(
        task_id = 'empty_6'
    )

    empty_2 >> Label('Start Branch') >> [empty_3, empty_4, empty_5] >> Label('End Branch') >> empty_6