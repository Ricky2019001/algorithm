from pyspark import SparkContext
from pyspark import SparkConf


conf = SparkConf().setAppName("yasaka").setMaster("local")
sc = SparkContext(conf=conf)

sc.textFile("test.txt") \
    .flatMap(lambda line: line.split()) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda x, y: x+y) \
    .foreach(print)
