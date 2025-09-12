from pyspark import SparkContext,SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "D:/Anaconda/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1,2,3,4,5])

rdd2 = rdd.filter(lambda num: num % 2 == 0)

print(rdd2.collect())