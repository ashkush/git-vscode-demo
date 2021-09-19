import numpy as np 
from pyspark.sql import SparkSession 
from pyspark.sql import functions
from pyspark import SparkContext

spark = SparkSession.builder.getOrCreate()

print(2+3)


print("in the name of the chrome")

sc = SparkContext


data = sc.parallelize([1,2,34,5],4)
print(data.getNumPartitions())
