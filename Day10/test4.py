from pyspark import SparkConf,SparkContext
conf = SparkConf().setMaster("local[*]").setAppName("test")
sc = SparkContext(conf=conf)
rdd = sc.textFile("D:/abc.txt")
print(rdd.collect())
sc.stop()