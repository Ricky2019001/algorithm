# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：TEST -> pool
@IDE    ：PyCharm
@Author ：Mr. Wang
@Date   ：2020/3/8 7:24 下午
@Desc   ：实现任务处理线程
=================================================='''
import psutil

import threading
from operate_system.task import Task, AsyncTask
from operate_system.queue import ThreadSafeQueue
#任务处理线程
class ProcessThread(threading.Thread):

    def __init__(self, task_queue, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        # 任务线程停止标记
        self.dismiss_flag = threading.Event()
        # 任务队列（线程从队列不断取出元素进行处理）
        self.task_queue = task_queue
        self.args = args
        self.kwargs = kwargs


    def run(self):
        while True:
            # 判断线程是否被要求停止
            if self.dismiss_flag.is_set():
                break
            task = self.task_queue.pop()
            if not isinstance(task, Task):
                continue
            # 执行task实际逻辑是通过函数调用引进来
            result = task.callable(*task.args, **task.kwargs)

            #异步任务
            if isinstance(task, AsyncTask):
                task.set_result(result)
    def dismiss(self):
        self.dismiss_flag.set()

    def stop(self):
        self.dismiss()


#实现线程池
class ThreadPool:

    def __init__(self, size=0):
        if not size:
            # 约定大小为CPU核数的2倍
            size = psutil.cpu_count() * 2
        # 线程池
        self.pool = ThreadSafeQueue(size)
        # 任务队列
        self.task_queue = ThreadSafeQueue()

        for i in range(size):
            self.pool.put(ProcessThread(self.task_queue))

    #启动线程池
    def start(self):
        for i in range(self.pool.size()):
            thread = self.pool.get(i)
            thread.start()

    # 停止线程池
    def join(self):
        for i in range(self.pool.size()):
            thread = self.pool.get(i)
            thread.stop()
        # 线程不为空，等待停止
        while self.pool.size():
            thread = self.pool.pop()
            thread.join()

    # 向线程池提交任务,向task_queue提交任务
    def put(self, item):
        if not isinstance(item, Task):
            raise TaskTypeErrorException()
        self.task_queue.put(item)

    # 批量提交
    def batch_put(self, item_list):
        if not isinstance(item_list, list):
            item_list = list(item_list)
        for item in item_list:
            self.put(item)

    def size(self):
        return self.pool.size()



class TaskTypeErrorException(Exception):
    pass
# 测试

if __name__ == "__main__":
    pass