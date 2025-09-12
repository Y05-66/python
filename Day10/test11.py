from pyspark import SparkContext, SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "D:/Anaconda/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test")
sc = SparkContext(conf=conf)

rdd = sc.textFile("D:/abc.txt")
# 对结果进行扁平化
word_rdd = rdd.flatMap(lambda x:x.split(" "))
# 对结果进行映射
word_with_one_rdd = word_rdd.map(lambda word:  (word, 1))
#  对结果进行聚合
result_rdd = word_with_one_rdd.reduceByKey(lambda a,b:a+b)
# 对结果进行排序
final_rdd = result_rdd.sortBy(lambda x:x[1], ascending=False,  numPartitions=1)

print(result_rdd.collect())