# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：TEST -> test
@IDE    ：PyCharm
@Author ：Mr. Wang
@Date   ：2020/3/8 8:23 下午
@Desc   ：用例测试
=================================================='''
from operate_system import task, pool

import time

class SimpleTask(task.Task):
    def __init__(self, callable):
        super(SimpleTask, self).__init__(callable)

def process():
    time.sleep(1)
    print("this is a SimpleTask callable function 1.")
    time.sleep(1)
    print("this is a SimpleTask callable function 2.")

def test():

    # 1. 初始化一个线程池
    test_pool = pool.ThreadPool()
    test_pool.start()

    # 2. 生成一系列的任务
    for i in range(10):
        simple_task = SimpleTask(process)
        # 3. 向线程池提交任务执行
        test_pool.put(simple_task)


def async_process():
    num = 0
    for i in range(100):
        num += i
    return num

def async_process2():
    num = 0
    for i in range(100):
        num += i
    return num

def async_process3():
    num = 0
    for i in range(100):
        num += i
    time.sleep(5)
    return num

def async_test():

    # 1. 初始化一个线程池
    test_pool = pool.ThreadPool()
    test_pool.start()

    # 2. 生成一系列的任务
    for i in range(10):
        async_task = task.AsyncTask(func=async_process)
        test_pool.put(async_task)
        result = async_task.get_result()
        print('Get result: %d' % result)

# 测试是否可以真正等待(wait)
def async_test2():
    # 1. 初始化一个线程池
    test_pool = pool.ThreadPool()
    test_pool.start()

    # 2. 生成一系列的任务
    for i in range(1):
        async_task = task.AsyncTask(func=async_process2)
        test_pool.put(async_task)
        print("before get result in timestamp: %d" % time.time())
        result = async_task.get_result()
        print("after get result in timestamp: %d, result: %d" % (time.time(), result))
        #print('Get result: %d' % result)

# 测试没有等待也可以获取结果
def async_test3():
    # 1. 初始化一个线程池
    test_pool = pool.ThreadPool()
    test_pool.start()

    # 2. 生成一系列的任务
    for i in range(1):
        async_task = task.AsyncTask(func=async_process3)
        test_pool.put(async_task)
        print("before get result in timestamp: %d" % time.time())
        time.sleep(5)
        # 可能主线程去做其它事情
        result = async_task.get_result()
        print("after get result in timestamp: %d, result: %d" % (time.time(), result))
        #print('Get result: %d' % result)


if __name__ == "__main__":
    #test()
    #async_test()
    # 存在等待
    #async_test2()
    async_test3()