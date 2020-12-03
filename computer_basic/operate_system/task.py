# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：TEST -> task
@IDE    ：PyCharm
@Author ：Mr. Wang
@Date   ：2020/3/7 8:07 下午
@Desc   ：实现任务对象
=================================================='''

import uuid
import threading

class Task:

    # 实现基本任务对象
    def __init__(self, func, *args, **kwargs):
        #任务具体逻辑，通过函数引用传递进来
        self.callable = func
        self.id = uuid.uuid4()
        self.args = args
        self.kwargs = kwargs

    def __str__(self):
        return "Task id: "+str(self.id)
# 异步任务对象
class AsyncTask(Task):

    def __init__(self, func, *args, **kwargs):
        self.result = None
        self.condition = threading.Condition()
        super().__init__(func, *args, **kwargs)

    # 设置运行结果的
    def set_result(self, result):
        self.condition.acquire()
        self.result = result
        self.condition.notify()
        self.condition.release()

    # 获取任务结果
    def get_result(self):
        self.condition.acquire()
        if not self.result:
            self.condition.wait()
        result = self.result
        self.condition.release()
        return result

def my_function():
    print("this is task test.")

if __name__ == "__main__":
    task = Task(func=my_function())
    print(task)
