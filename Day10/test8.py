from pyspark import SparkContext, SparkConf
import os
os.environ['PYSPARK_PYTHON'] = "D:/Anaconda/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test")
sc = SparkContext(conf=conf)

rdd = sc.textFile("D:/abc.txt")

word_rdd = rdd.flatMap(lambda x:x.split(" "))

word_with_one_rdd = word_rdd.map(lambda word:  (word, 1))

result_rdd = word_with_one_rdd.reduceByKey(lambda a,b:a+b)

print(result_rdd.collect())