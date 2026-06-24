from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PySpark Learning") \
    .getOrCreate()

print(f"Spark Version: {spark.version}")

spark.stop()