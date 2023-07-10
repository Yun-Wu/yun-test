from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonVirtualenvOperator

default_args = {
    'owner': 'yun',
    'retries': 0,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='dag_with_traj_v01',
    default_args=default_args,
    start_date=datetime(2023, 7, 9),
    schedule_interval='0 0 * * *'
) as dag:
    
    def execute_notebook():
        import papermill as pm

        pm.execute_notebook(
            'https://github.com/Yun-Wu/yun-test/blob/main/trajectory_example.ipynb',
            '/home/airflow/gcs/data/out.ipynb'
        )

    # [START howto_operator_papermill]
    run_this = PythonVirtualenvOperator(
        task_id="virtualenv_classic",
        requirements=['ecoscope', 'papermill', 'shapely==2.0.1', 'pandas', 'apache-airflow'],
        python_callable=execute_notebook,
    )
    # [END howto_operator_papermill]