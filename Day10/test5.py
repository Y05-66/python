from pyspark import SparkContext, SparkConf
import os

os.environ['PYSPARK_PYTHON'] = "D:/Anaconda/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1, 2, 3, 4, 5])

# def func(x):
#     return x * 10


# rdd1 = rdd.map(func)

rdd2 = rdd.map(lambda x: x * 10)
print(rdd2.collect())
sc.stop()
