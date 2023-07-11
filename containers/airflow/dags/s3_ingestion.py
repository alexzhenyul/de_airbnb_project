from datetime import datetime
from airflow.models import DAG
from airflow.operators.python import PythonOperator
from airflow,hooks.s3_hook import S3Hook

def upload_to_s3(filename:str, key:str, bucket_name:str) -> None:
    hook = S3Hook('s3_conn')
    hook.load_file(filename=filename, key=key, bucket_name=bucket_name)

with DAG(
    dag_id = 's3_ingestion_dag'
    schedule_interval = '@once'
    start_date = datetime(2023, 07, 12), 
    catchup = False
) as dag:
    
    data_upload_to_s3 = PythonOperator(
        task_id = 'upload_to_s3', 
        python_callable = upload_to_s3, 
        op_kwargs={
            'filename': '~/de_airbnb_project/data/*', 
            'key': 'csv', 
            'bucket_name': 'stage-bucket-alexl'
        }
    )
