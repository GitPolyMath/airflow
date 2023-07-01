from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from common.common_func import regist2


with DAG(
    dag_id = "dags_python_with_op_kwargs" ,
    schedule = "30 6 * * *",
    start_date = pendulum.datetime(2023, 7, 1, tz = "Asia/Seoul"),
    catchup = False
) as dag:

    regist_t2 = PythonOperator(
        task_id = 'regist_2',
        python_callable=regist2,
        op_args = ['matthew', 'Male', 'kr' ,'seoul'],
        op_kwargs={'email':'kakakuku@gmail.com', 'phone':'010-1234-5678'}
    )

    regist_t2