from airflow import DAG
# from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime  import datetime
# from codes.dag_functions import QuakeFunctions
from codes.python_functions import CumtomPyFunctions



default_args = {'start_date':datetime(2023,1,1),
    'end_date':datetime(2023,1,1),}
extract_ApiQuake = CumtomPyFunctions.extract_ApiQuake
interest_info = CumtomPyFunctions.interest_info
#TODO Mpver todo esto a un docker mas la instalacion de airflow.


with DAG (
    dag_id="DashboardQuake",
    description="Extraccion de datos de distintas fuentes para la construccion de un Dashboard",
    schedule_interval="@daily", #puede ser cron tambien! si quiero que se ejecute cada 5 min todos los lunes seria 5***1

    default_args=default_args,
    max_active_runs=1
    ) as dag:

# Tarea que extrae datos de una api y transforma en un dataframe y se dispara despues de una suscripcion mediante un correo electronico
#TODO revisar BashPythonOperator y como disparar un proceso cuando se optenga un dato, eso es el correo electronico ingresado mediante una casilla de texto
    t1 = PythonOperator(
        task_id="ApiQuake",
        python_callable=extract_ApiQuake,
        retries= 1,
        retry_delay= 5,
        # :trigger_rule=TriggerRule.ALL_SUCCESS,
        depends_on_past=False
    )

    t2 = PythonOperator(
        task_id="ApiWiki",
        python_callable=interest_info,
        retries= 1,
        retry_delay= 5,
        # :trigger_rule=TriggerRule.ALL_SUCCESS,
        depends_on_past=False
    )

    t1 >> t3