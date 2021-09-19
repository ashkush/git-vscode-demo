import numpy as np 
from pyspark.sql import SparkSession 
from pyspark.sql import functions
from pyspark import SparkContext

spark = SparkSession.builder.getOrCreate()


sc = SparkContext


data = sc.parallelize([1,2,34,5],4)
print(data.getNumPartitions())
