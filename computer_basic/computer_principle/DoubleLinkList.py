#! -*- encoding=utf-8 -*-

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.pre = None
        self.next = None

    def __str__(self):
        val = '{%s, %d}' % (self.key, self.value)
        return val

    def __repr__(self):
        val = '{%s, %d}' % (self.key, self.value)
        return val



class DoubleLinkedList:
    def __init__(self, capacity = 0xffff):
        self.capacity = capacity
        self.head = Node
        self.tail = Node
        self.size = 0

    # 头部增加节点
    def __add_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
            self.head.pre = Node
            self.tail.next = Node
        else:
            node.next = self.head
            self.head.pre = node
            self.head = node
            self.head.pre = None
        self.size += 1
        return node

    # 尾部增加节点
    def __add_tail(self, node):
        if not self.tail:
            self.head = node
            self.tail = node
            self.tail.pre = None
            self.tail.next = None
        else:
            self.tail.next = node
            node.pre = self.tail
            self.tail = node
            self.tail.next = None
        self.size += 1
        return node

    # 尾部删除
    def __del_tail(self):
        if not self.tail:
            return
        node = self.tail
        if node.pre:
            self.tail = node.pre
            self.tail.next = None
        else:
            self.tail = self.head = None
        self.size -= 1
        return node

    # 头部节点删除
    def __del_head(self):
        if not self.head:
            return
        node = self.head
        if node.next:
            self.head = node.next
            self.head.pre = None
        else:
            self.head = self.tail = None
        self.size -= 1
        return node


    # 删除任意节点
    def __del_any(self, node):
        # 如果节点不存在，删除尾部节点
        if not node:
            node = self.tail
        if node == self.tail:
            self.__del_tail()
        elif node == self.head:
            self.__del_head()
        else:
            node.pre.next = node.next
            node.next.pre = node.pre
        self.size -= 1
        return node

    # 公用API
    # 弹出头部节点
    def pop(self):
        return self.__del_head()

    # 添加节点
    def append(self, node):
        return self.__add_tail(node)

    # 头部添加节点
    def append_front(self, node):
        return self.__add_head(node)

    #删除节点
    def del_node(self, node=None):
        return self.__del_any(node)

    def print(self):
        p = self.head
        line = ''
        while p:
            line += '%s' % p
            p = p.next
            if p:
                line += '=>'
        print(line)


# 测试,pop（）时，发现<class '__main__.Node'>=>{0, 0}
if __name__ == '__main__':
    lst = DoubleLinkedList(10)
    nodes = []
    for i in range(10):
        node = Node(i, i)
        nodes.append(node)
    lst.append(nodes[0])
    lst.print()
    lst.pop()
    lst.print()
    lst.append(nodes[1])
    lst.print()
    lst.pop()
    lst.print()
    lst.append(nodes[2])
    lst.print()
    lst.append_front(nodes[3])
    lst.print()
    lst.append(nodes[4])
    lst.print()
    lst.del_node(nodes[2])
    lst.print()
    lst.del_node()
    lst.print()




