# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：TEST -> LRUCache
@IDE    ：PyCharm
@Author ：Mr. Wang
@Date   ：2020/2/21 10:01 下午
@Desc   ：最近最少使用算法
(1) 1               （6）6、4、5、7 [2]
(2) 2、1             (1) 1、6、4、5 [7]
(3)4、2、1            (6) 6、1、4、5
(7)7、4、2、1         (7) 7、6、1、4 [5]
(5)5、7、4、2 [1]    （4）4、7、6、1
(4)4、5、7、2        （1）1、4、7、6

capacity = 4,()使用的字块，[]置换掉的字块
=================================================='''


from computer_principle.DoubleLinkList import DoubleLinkedList, Node


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.list = DoubleLinkedList(self.capacity)

    def get(self, key):
        if key in self.map:
            node = self.map.get(key)
            self.list.del_node(node)
            self.list.append_front(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        if key in self.map:
            node = self.map.get(key)
            self.list.del_node(node)
            self.map[key] = value
            self.list.append_front(Node(key, value))
            print(Node(key, value))
        else:
            node = Node(key, value)
            print(node)
            # size是否为capacity
            if self.list.size >= self.list.capacity:
                rev_node = self.list.del_node()
                self.map.pop(rev_node.key)
                print(self.map.pop(rev_node.key))
            #满不满都操作
            self.list.append_front(node)
            self.map[key] = node         #node.value

    def print(self):
        pass#self.list.print()


if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(1, 2)
    #cache.print()
    '''cache.print()
    cache.put(1, 1)
    cache.print()
    cache.put(3, 3)
    cache.print()
    print(cache.get(1))
    cache.print()
    print(cache.get(2))
    cache.print()
    print(cache.get(3))
    cache.print()
'''

