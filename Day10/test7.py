from pyspark import SparkContext, SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "D:/Anaconda/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([('男',99),('男',88),('女',99),('女',88)])

rdd2 = rdd.groupByKey(lambda a, b: a + b)
print(rdd2.collect())