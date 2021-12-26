import psycopg2
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
def insertar():  
    query = """ 
    INSERT INTO public.airflow (dt) VALUES(NOW())
    """
    conexion1 = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="dalealbo")
    cursor1=conexion1.cursor()
    cursor1.execute(query)
    conexion1.commit()
    conexion1.close()
    print('¡DT Insertado')
    
dag = DAG('insertar_postgres', 
description='Postgres Insert DAG',
schedule_interval='*/1 * * * *',
start_date=datetime(2021, 12, 26),
catchup=False,)
insertar_operator = PythonOperator(task_id='insert_task', python_callable=insertar, dag=dag)


