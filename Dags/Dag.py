from airflow import DAG
from datetime import datetime 
from airflow.operators.bash import BashOperator
from airflow.providers.amazon.aws.transfers.sql_to_s3 import SqlToS3Operator
from datetime import datetime, timedelta
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.providers.snowflake.operators.snowflake import SnowflakeOperator

import sys
sys.path.append('/opt/airflow/inclueds')

from emp_dim_insert_update import *
from queries import *


def check_ids_to_update():
    if ids_to_update == "":
        return 'dum'
    else:
        return 'snowflake_update'


@task()
def main_data():
    join_and_detect_new_or_changed_rows()
    
    
with DAG("project_f", start_date= datetime(2023,5,14), schedule='@hourly' , catchup=False) as dag:
    task1=SqlToS3Operator (
    task_id="sql_to_s3_task_finance",
    aws_conn_id ='islam_aws',
    sql_conn_id='islam_postgress',
    query="select * from finance.emp_sal ",
    s3_bucket='staging.emp.data',
    s3_key='islam_finance.csv',
    replace=True,
    )
    
    task2=SqlToS3Operator (
    task_id="sql_to_s3_task_postgres",
    aws_conn_id ='islam_aws',
    sql_conn_id='islam_postgress',
    query="select * from hr.emp_details ",
    s3_bucket='staging.emp.data',
    s3_key='islam_hr.csv',
    replace=True,
    )
    
    task3 = BashOperator(task_id='bash_task_1', bash_command='echo end')
    data = join_and_detect_new_or_changed_rows()
    rows_to_insert = data["rows_to_insert"]
    ids_to_update = data["ids_to_update"]
    rows_insert = queries.INSERT_INTO_DWH_EMP_DIM(rows_to_insert)
    rows_upd = queries.UPDATE_DWH_EMP_DIM(ids_to_update)
    
    insert = SnowflakeOperator(task_id="snowflake_insert", sql=rows_insert, snowflake_conn_id="islam_snow", trigger_rule = "none_failed")
    update = SnowflakeOperator(task_id="snowflake_update", sql=rows_upd, snowflake_conn_id="islam_snow")
    dummy=DummyOperator(task_id="dum")
    
    branch = BranchPythonOperator(
        task_id='check_ids_to_update',
        python_callable=check_ids_to_update,
        dag=dag
    )
    
    
    [task1, task2] >> data >> branch >> [dummy, update] >> insert >> task3
    
    