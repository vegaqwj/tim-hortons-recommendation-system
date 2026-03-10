
from pyspark.sql import SparkSession

spark = SparkSession.builder     .appName("recsys_training")     .getOrCreate()

user_features = spark.read.parquet("features/user_features")
product_features = spark.read.parquet("features/product_features")

dataset = user_features.join(product_features)

dataset.show()
