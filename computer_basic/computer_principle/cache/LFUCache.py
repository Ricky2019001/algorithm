# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：TEST -> LFUCache
@IDE    ：PyCharm
@Author ：Mr. Wang
@Date   ：2020/2/24 3:20 下午
@Desc   ：最不经常使用算法
        淘汰缓存时，把使用频率最小的淘汰
        记录频率，把相同的频率放在container,同频率按照fifo淘汰
=================================================='''

from computer_principle.DoubleLinkList import DoubleLinkedList, Node

class LFUNode(Node):
    def __init__(self, key, value):
        self.freq = 0
        super(LFUNode, self).__init__(key, value)

class LFUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        # key:频率，value:频率对应的双向链表
        self.freq_map = {}
        self.size = 0

    #更新节点频率
    def __freq_update(self, node):
        freq = node.freq

        #删除
        node = self.freq_map[freq].remove()
        if self.freq_map[freq].size == 0:
            del self.freq_map[freq]

        #更新
        freq += 1
        node.freq = freq
        if freq not in self.freq_map:
            self.freq_map[freq] = DoubleLinkedList()
        self.freq_map[freq].append(node)

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map.get(key)
        self.__freq_update(node)
        return node.value

    def put(self, key, value):
        if self.capacity == 0:
            return

        #缓存命中
        if key in self.map:
            node = self.map.get(key)
            node.value = value
            self.__freq_update(node)
        #命不中缓存
        else:
           if self.capacity == self.size:
               min_freq = min(self.freq_map)
               node = self.freq_map[min_freq].pop()
               #本地映射删掉
               del self.map[node.key]
               self.size -= 1
           node = LFUNode(key, value)
           node.freq = 1
           self.freq_map[key] = node
           if node.freq not in self.freq_map:
               self.freq_map[node.freq] = DoubleLinkedList()
           node = self.freq_map[node.freq].append(node)
           self.size += 1

    def print(self):
        print('+++++++++++++++++++++++++')
        for k, v in self.freq_map.items():
            print('Fre = %d', k)
            self.freq_map[k].print()
        print('-------------------------')
        print()

#测试
if __name__ == '__main__':
    cache = LFUCache(4)
    cache.put(1, 1)
    cache.print()
    cache.put(2, 2)
    cache.print()
    print(cache.get(1))
    cache.print()
    cache.put(3, 3)
    cache.print()
    print(cache.get(2))
    cache.print()
    print(cache.get(3))
    cache.print()
    cache.put(4, 4)
    cache.print()
    print(cache.get(1))
    cache.print()
    print(cache.get(3))
    cache.print()
    print(cache.get(4))
    cache.print()



