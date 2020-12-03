# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：TEST -> FIFOCache
@IDE    ：PyCharm
@Author ：Mr. Wang
@Date   ：2020/2/20 10:27 下午
@Desc   ：
=================================================='''


from computer_principle.DoubleLinkList import DoubleLinkedList, Node


class FIFOCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.map = {}
        self.list = DoubleLinkedList(self.capacity)

    def get(self, key):
        if not key in self.map:
            return -1
        else:
            node = self.map.get(key)
            return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return
        if key in self.map:
            node = self.map.get(key)
            self.list.del_node(node)
            self.list.append(Node(key, value))
        else:
            if self.size == self.capacity:
                node = self.list.pop()
                del self.map[node.key]
                self.size -= 1
            else:
                node = Node(key, value)
                self.list.append(node)
                self.map[key] = node
                self.size += 1

    def print(self):
        self.list.print()


# 测试
if __name__ == '__main__':
    cache = FIFOCache(8)
    cache.put('a', 1)
    cache.print()
    cache.put('b', 1)
    cache.print()
    cache.put('a', 2)
    cache.print()