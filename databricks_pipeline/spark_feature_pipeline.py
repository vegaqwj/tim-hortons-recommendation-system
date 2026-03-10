
from pyspark.sql import SparkSession
from pyspark.sql.functions import count

spark = SparkSession.builder     .appName("recsys_feature_pipeline")     .getOrCreate()

orders = spark.read.csv("data/orders.csv", header=True, inferSchema=True)

# user features
user_features = orders.groupBy("user_id")     .agg(count("*").alias("total_orders"))

# product popularity
product_features = orders.groupBy("product_id")     .agg(count("*").alias("product_popularity"))

user_features.write.mode("overwrite").parquet("features/user_features")
product_features.write.mode("overwrite").parquet("features/product_features")
