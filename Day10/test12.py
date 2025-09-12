from pyspark import SparkContext,SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "D:/Anaconda/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test")
sc = SparkContext(conf=conf)

rdd = sc.parallelize([1,2,3,4,5])
# collect(), 返回一个列表
rdd_list: list = rdd.collect()
print(rdd_list)
print(type(rdd_list))
# reduce()，对RDD进行聚合操作
num = rdd.reduce(lambda x,y: x+y)
print(num)
# take()，取出前n个元素
take_list = rdd.take(3)
print(take_list)
# count()，统计元素个数
num_count = rdd.count()
print(f"rdd内有{num_count}个元素")

sc.stop()