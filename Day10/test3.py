from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local[*]").setAppName("test")
sc = SparkContext(conf=conf)

rdd1 = sc.parallelize([1,2,3,4,5])
rdd2 = sc.parallelize((1,2,3,4,5))
rdd3 = sc.parallelize({1,2,3,4,5})
rdd4 = sc.parallelize("hello world")
rdd5 = sc.parallelize({"hello":1, "world":2})

print(rdd1.collect())
print(rdd2.collect())
print(rdd3.collect())
print(rdd4.collect())
print(rdd5.collect())

sc.stop()