
from pyspark.sql import SparkSession

spark = SparkSession.builder     .appName("recsys_inference")     .getOrCreate()

users = spark.read.parquet("features/user_features")

users.show()
