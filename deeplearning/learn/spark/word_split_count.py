from pyspark import SparkConf
from pyspark import SparkContext

conf = SparkConf().setAppName("word").setMaster("local")
sc = SparkContext(conf=conf)
# sc.setLogLevel("INFO")
# rd = sc.textFile('test.txt')
# print(type(rd))
# rd1 = rd.map(lambda x: x.split(' '))
# rd2 = rd.flatMap(lambda x: x.split(' ')).glom()
# ret = rd2.collect()
# print(ret)

L = [1, 2, 3, 4]
old = sc.parallelize(L, 2)
"""
parallelize()函数将一个List列表转化为了一个RDD对象，collect()函数将这个RDD对象转化为了一个List列表。
parallelize()函数的第二个参数表示分区，默认是1，此处为2，表示将列表对应的RDD对象分为两个区。
后面的glom()函数就是要显示出RDD对象的分区情况，可以看出分了两个区，如果没有glom()函数，则不显示分区，如第一个结果所示。

"""
print(old.collect())
print(old.glom().collect())

#  map()和reduce()
"""
map()类似于Python中的map，针对RDD对应的列表的每一个元素，进行map()函数里面的lamda函数（这个函数是map函数的一个参数）对应的操作，返回的仍然是一个RDD对象。
reduce()是针对RDD对应的列表中的元素，递归地选择第一个和第二个元素进行操作，操作的结果作为一个元素用来替换这两个元素，注意，reduce返回的是一个Python可以识别的对象，非RDD对象。

"""
rdd_1 = sc.parallelize(L, 1)
print(rdd_1.reduce(lambda a,b: a+b))
print(rdd_1.map(lambda x: (x, x**2)).collect())

# map()和flatMap()
rdd_2=sc.parallelize(L, 2)
print(rdd_2.glom().collect())
print("map:", rdd_2.map(lambda x: (x, x**2)).glom().collect())
print("faltMap:", rdd_2.flatMap(lambda a: (a, a+2)).glom().collect())

# filter()和distinct()
"""
filter()用于删除/过滤，即删除不满足条件的元素，这个条件一lambda函数的形式作为参数传入filter()函数中。
distinct()用于去重，没有参数。
"""
rdd_3 = sc.parallelize(L, 1)
print("filter:", rdd_3.filter(lambda x: x % 2 == 1).collect())
rdd_4 = rdd_3.flatMap(lambda x: (x, x + 2, x ** 2))
print(rdd_4.collect())
print("distinct:", rdd_4.distinct().collect())


# reduce()、reduceByKey()和reduceByKeyLocally()
"""
reduce()前面讲过，即最终只返回一个值，reduceByKey()和reduceByKeyLocally()均是将Key相同的元素合并。
区别在于，reduce()和reduceByKeyLocally()函数均是将RDD转化为非RDD对象，而reduceByKey()将RDD对象转化为另一个RDD对象，需要collect()函数才能输出
"""
rdd_5 = sc.parallelize([(1, 2), (1, 3), (3, 4), (3, 6)])
rdd_6 = rdd_5.reduceByKey(lambda x, y: x+y)
print("rdd_5", rdd_5.collect())
print("reduceByKey",rdd_6.collect())
