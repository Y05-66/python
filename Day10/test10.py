from pyspark import SparkContext,SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "D:/Anaconda/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1,2,3,4,5,3,5,2,1])
# 对rdd去重
rdd2 = rdd.distinct()

print(rdd2.collect())