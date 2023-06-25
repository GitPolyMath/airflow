from airflow import DAG
import pendulum
import datetime
from airflow.operators.email import EmailOperator

with DAG(
    dag_id = "dags_bash_select_fruit",
    schedule = "0 8 * 1 1#1",
    start_date = pendulum.datetime(2023, 3, 1, tz="Asia/Seoul"),
    catchup = False
) as dag:

    send_email_task = EmailOperator(
        task_id = "t1_orange",
        to = 'matthew@wink.kr',
        subject = '(matthew Airflow작업)[Airflow 성공메일]',
        html_content = 'Airflow 작업테스트가 완료되었습니다.',
    )