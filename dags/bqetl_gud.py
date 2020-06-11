# Generated via https://github.com/mozilla/bigquery-etl/blob/master/bigquery_etl/query_scheduling/generate_airflow_dags.py

from airflow import DAG
from airflow.operators.sensors import ExternalTaskSensor
import datetime
from utils.gcp import bigquery_etl_query

default_args = {
    "owner": "jklukas@mozilla.com",
    "start_date": datetime.datetime(2019, 7, 25, 0, 0),
    "email": ["telemetry-alerts@mozilla.com", "jklukas@mozilla.com"],
    "depends_on_past": False,
    "retry_delay": datetime.timedelta(seconds=300),
    "email_on_failure": True,
    "email_on_retry": True,
    "retries": 1,
}

with DAG("bqetl_gud", default_args=default_args, schedule_interval="0 1 * * *") as dag:

    telemetry_derived__smoot_usage_desktop__v2 = bigquery_etl_query(
        task_id="telemetry_derived__smoot_usage_desktop__v2",
        destination_table="smoot_usage_desktop_v2",
        dataset_id="telemetry_derived",
        project_id="moz-fx-data-shared-prod",
        owner="jklukas@mozilla.com",
        email=["jklukas@mozilla.com"],
        date_partition_parameter="submission_date",
        depends_on_past=False,
        dag=dag,
    )

    telemetry_derived__smoot_usage_new_profiles__v2 = bigquery_etl_query(
        task_id="telemetry_derived__smoot_usage_new_profiles__v2",
        destination_table="smoot_usage_new_profiles_v2",
        dataset_id="telemetry_derived",
        project_id="moz-fx-data-shared-prod",
        owner="jklukas@mozilla.com",
        email=["jklukas@mozilla.com"],
        date_partition_parameter="submission_date",
        depends_on_past=False,
        dag=dag,
    )

    telemetry_derived__smoot_usage_desktop_compressed__v2 = bigquery_etl_query(
        task_id="telemetry_derived__smoot_usage_desktop_compressed__v2",
        destination_table="smoot_usage_desktop_compressed_v2",
        dataset_id="telemetry_derived",
        project_id="moz-fx-data-shared-prod",
        owner="jklukas@mozilla.com",
        email=["jklukas@mozilla.com"],
        date_partition_parameter="submission_date",
        depends_on_past=False,
        dag=dag,
    )

    telemetry_derived__smoot_usage_new_profiles_compressed__v2 = bigquery_etl_query(
        task_id="telemetry_derived__smoot_usage_new_profiles_compressed__v2",
        destination_table="smoot_usage_new_profiles_compressed_v2",
        dataset_id="telemetry_derived",
        project_id="moz-fx-data-shared-prod",
        owner="jklukas@mozilla.com",
        email=["jklukas@mozilla.com"],
        date_partition_parameter="submission_date",
        depends_on_past=False,
        dag=dag,
    )

    telemetry_derived__smoot_usage_nondesktop_compressed__v2 = bigquery_etl_query(
        task_id="telemetry_derived__smoot_usage_nondesktop_compressed__v2",
        destination_table="smoot_usage_nondesktop_compressed_v2",
        dataset_id="telemetry_derived",
        project_id="moz-fx-data-shared-prod",
        owner="jklukas@mozilla.com",
        email=["jklukas@mozilla.com"],
        date_partition_parameter="submission_date",
        depends_on_past=False,
        dag=dag,
    )

    telemetry_derived__smoot_usage_nondesktop__v2 = bigquery_etl_query(
        task_id="telemetry_derived__smoot_usage_nondesktop__v2",
        destination_table="smoot_usage_nondesktop_v2",
        dataset_id="telemetry_derived",
        project_id="moz-fx-data-shared-prod",
        owner="jklukas@mozilla.com",
        email=["jklukas@mozilla.com"],
        date_partition_parameter="submission_date",
        depends_on_past=False,
        dag=dag,
    )

    wait_for_main_summary_clients_last_seen = ExternalTaskSensor(
        task_id="wait_for_main_summary_clients_last_seen",
        external_dag_id="main_summary",
        external_task_id="clients_last_seen",
        check_existence=True,
        mode="reschedule",
        dag=dag,
    )

    telemetry_derived__smoot_usage_desktop__v2.set_upstream(
        wait_for_main_summary_clients_last_seen
    )

    telemetry_derived__smoot_usage_new_profiles__v2.set_upstream(
        telemetry_derived__smoot_usage_desktop__v2
    )

    telemetry_derived__smoot_usage_new_profiles__v2.set_upstream(
        telemetry_derived__smoot_usage_nondesktop__v2
    )

    telemetry_derived__smoot_usage_desktop_compressed__v2.set_upstream(
        telemetry_derived__smoot_usage_desktop__v2
    )

    telemetry_derived__smoot_usage_new_profiles_compressed__v2.set_upstream(
        telemetry_derived__smoot_usage_new_profiles__v2
    )

    telemetry_derived__smoot_usage_nondesktop_compressed__v2.set_upstream(
        telemetry_derived__smoot_usage_nondesktop__v2
    )

    wait_for_telemetry_derived__core_clients_last_seen__v1 = ExternalTaskSensor(
        task_id="wait_for_telemetry_derived__core_clients_last_seen__v1",
        external_dag_id="bqetl_core",
        external_task_id="telemetry_derived__core_clients_last_seen__v1",
        check_existence=True,
        mode="reschedule",
    )

    telemetry_derived__smoot_usage_nondesktop__v2.set_upstream(
        wait_for_telemetry_derived__core_clients_last_seen__v1
    )
    wait_for_copy_deduplicate_baseline_clients_last_seen = ExternalTaskSensor(
        task_id="wait_for_copy_deduplicate_baseline_clients_last_seen",
        external_dag_id="copy_deduplicate",
        external_task_id="baseline_clients_last_seen",
        check_existence=True,
        mode="reschedule",
        dag=dag,
    )

    telemetry_derived__smoot_usage_nondesktop__v2.set_upstream(
        wait_for_copy_deduplicate_baseline_clients_last_seen
    )