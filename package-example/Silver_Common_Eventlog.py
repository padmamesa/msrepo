"""Define python file for silver_common_eventlog."""
from shsmr.common import spark_utils

spark_session = spark_utils.get_spark_session()

print("OK")
