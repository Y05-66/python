from pyspark import SparkContext, SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "D:/Anaconda/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test")
sc = SparkContext(conf=conf)

rdd = sc.parallelize(["张三 12", "李四 13", "王五 14"])
rdd = rdd.flatMap(lambda x: x.split(" "))
print(rdd.collect())