# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：TEST -> server
@IDE    ：PyCharm
@Author ：Mr. Wang
@Date   ：2020/3/8 11:14 下午
@Desc   ：
=================================================='''
import socket
import json

from operate_system.pool import ThreadPool as tp
from operate_system.task import AsyncTask
from computer_network.process.net.parser import IPParser

class ProcessTask(AsyncTask):

    def __init__(self, packet, *args, **kwargs):
        self.packet =packet
        #AsyncTask(func=self.process, *args, **kwargs)
        super(AsyncTask, self).__init__(func=self.process, *args, **kwargs)


     # 报文处理
    def process(self):
        ip_header = IPParser.parse(self.packet)
        return ip_header



class Server:

    def __init__(self):
        # 参数：工作协议类型、套接字类型和工作具体协议
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_RAW,
                                  socket.IPPROTO_TP)

        self.ip = '192.168.1.110'
        self.port = 8888
        self.sock.bind((self.ip, self.port))

        #网卡设置混杂模式
        self.sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        #创建一个线程池并启动
        self.pool = tp(10)
        self.pool.start()

    def loop_serve(self):
        while True:
            # 接收
            packet, addr = self.sock.recvfrom(65535)
            # 生成
            task = ProcessTask(packet)
            # 提交
            self.pool.put(task)
            # 获取结过
            result = task.get_result()
            result = json.dump(
                result,
                indent=4
            )
            print(result)

if __name__ == '__main__':
    server = Server()
    server.loop_serve()