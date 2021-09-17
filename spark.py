from pyspark.sql import functions as f
from pyspark.sql import SparkSession


spark = SparkSession.builder.getOrCreate()

print(spark)


spark.createDataFrame