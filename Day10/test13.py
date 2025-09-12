from pyspark import SparkContext, SparkConf
import os

os.environ['PYSPARK_PYTHON'] = "D:/Anaconda/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test")
conf.set("spark.default.parallelism", 1)
sc = SparkContext(conf=conf)

# 读取文件转换成DRR
file_rdd = sc.textFile("D:abc.txt")
# TODO 需求1：热门搜索时间段Top3(小时精度)
result1 = file_rdd.map(lambda x: (x.split("\t")[0][:2], 1)). \
    reduceByKey(lambda x, y: x + y). \
    sortBy(lambda x: x[1], ascending=False). \
    take(3)
print(result1)

# TODO 需求2：热门搜索词Top3
result2 = file_rdd.map(lambda x: (x.split("\t")[2], 1)). \
    reduceByKey(lambda x, y: x + y). \
    sortBy(lambda x: x[1], ascending=False, numPartitions=1). \
    take(3)
print(result2)

# TODO 需求3：统计黑马程序员关键词在什么时候被搜索的最多
result3 = file_rdd.filter(lambda x: x.split("\t")[2] == "黑马程序员"). \
    map(lambda x: (x.split("\t")[0], 1)). \
    reduceByKey(lambda x, y: x + y). \
    sortBy(lambda x: x[1], ascending=False, numPartitions=1). \
    take(1)
print(result3)

# TODO 需求4：将数据转换为JSON格式，写出到文件中
file_rdd.map(lambda x: x.split("\t")). \
    map(lambda x: {"time": x[0], "user_id": x[1], "key_word": x[2], "rank1": x[3], "rank2": x[4], "url": x[5]}). \
    saveAsTextFile("D:/output_json")
