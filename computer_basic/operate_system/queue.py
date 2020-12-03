# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：TEST -> queue
@IDE    ：PyCharm
@Author ：Mr. Wang
@Date   ：2020/3/5 11:21 下午
@Desc   ：实现线程安全队列
=================================================='''
import time
import threading

class ThreadSafeQueueException(Exception):
    pass

# 线程安全队列
class ThreadSafeQueue(object):

    def __init__(self, max_size = 0):
        self.queue = []
        self.max_size = max_size
        self.lock = threading.Lock()
        self.condition = threading.Condition()



    # 当前队列元素的数量
    def size(self):
        self.lock.acquire()
        size = len(self.queue)
        self.lock.release()
        return size

    # 往队列里面放入元素
    def put(self, item):
        if self.max_size !=0 and self.size() > self.max_size:
            return ThreadSafeQueueException()

        self.lock.acquire()
        self.queue.append(item)
        self.lock.release()
        # size = 0,存在组赛，加入后通知
        self.condition.acquire()
        self.condition.notify()
        self.condition.release()

    def batch_put(self, item_list):
        if not isinstance(item_list, list):
            item_list = list(item_list)
        for item in item_list:
            self.put(item)

    #从队列取出元素,默认不阻塞
    def pop(self, block = False, timeout = 0):
        if self.size() == 0:
            # 阻塞等待
            if  block:
                self.condition.acquire()
                self.condition.wait()
                self.condition.release()
            else:
                return None
        # 非 0
        self.lock.acquire()
        item = None
        if len(self.queue) > 0:
            item = self.queue.pop()
        self.lock.release()
        return item

    def get(self, index):
        self.condition.acquire()
        item = self.queue[index]
        self.condition.release()
        return item


# 测试
if __name__ == '__main__':
    queue = ThreadSafeQueue(max_size=100)

    def producer():
        while True:
            queue.put(1)
            time.sleep(100)

    def consumer():
        while True:
            item = queue.pop(block= True, timeout= 1)
            print('get item from queue: %d', item)
            time.sleep(1)
    thread1 = threading.Thread(target=producer)
    thread2 = threading.Thread(target=consumer)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()