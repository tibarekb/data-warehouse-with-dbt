# import airflow
# from datetime import timedelta
# from airflow import DAG
# from airflow.providers.postgres.operators.postgres import PostgresOperator
# from airflow.utils.dates import days_ago

# args={'owner': 'airflow'}

# default_args = {
#     'owner': 'airflow',    
#     #'start_date': airflow.utils.dates.days_ago(2),
#     # 'end_date': datetime(),
#     # 'depends_on_past': False,
#     #'email': ['airflow@example.com'],
#     #'email_on_failure': False,
#     # 'email_on_retry': False,
#     # If a task fails, retry it once after waiting
#     # at least 5 minutes
#     'retries': 1,
#     'retry_delay': timedelta(minutes=5),
# }

# with DAG(
#     dag_id = "postgres_with_airflow",
#     default_args=args,
#     schedule=None,	
#     dagrun_timeout=timedelta(minutes=60),
#     description='loading a csv file in to a postgresql',
#     start_date = airflow.utils.dates.days_ago(1)
# )as dag:

#     create_table = PostgresOperator(
#         sql = """
#             CREATE TABLE traffic_data(id INT NOT NULL, track_id INT NOT NULL, type VARCHAR(250) NOT NULL, traveled_d VARCHAR(250) NOT NULL, avg_speed VARCHAR(250) NOT NULL, lat VARCHAR(250) NOT NULL, lon VARCHAR(250) NOT NULL, speed VARCHAR(250) NOT NULL, lon_acc VARCHAR(250) NOT NULL, lat_acc VARCHAR(250) NOT NULL, time VARCHAR(250) NOT NULL);
#         """,
#         task_id = "create_table_task",
#         postgres_conn_id = "dbt_setup",
       
#     ),

#     insert_data = PostgresOperator(
#         sql = """
#                     COPY traffic_data(id, track_id, type, traveled_d, avg_speed, lat, lon, speed, lon_acc, lat_acc, time)
#                     FROM './traffic_data2.csv'
#                     DELIMITER ','
#                     CSV HEADER;
#               """,
#         task_id = "insert_data_task",
#         postgres_conn_id = "dbt_setup",
      
#     )


#     create_table 