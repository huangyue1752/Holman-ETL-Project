from airflow import DAG

from airflow.operators.python_operator import PythonOperator

from airflow.utils.dates import days_ago

from datetime import datetime
from Holman_FV import holman_ari

import requests



dag = DAG(

    'Holman_dag',

    default_args={'start_date': days_ago(1)},

    schedule_interval='00 11 22 * *',

    catchup=False

)



print_welcome_task = PythonOperator(

    task_id='Print_Holman_Data',

    python_callable=holman_ari,

    dag=dag

)


