class Node:
    def __init__(self, item):
        self.item = item  # 该节点值
        self.next = None   #  连接一下一个节点


class SinglyLinkedList:
    """链表对象"""
    def __init__(self):
        self.head = None

    def add(self, item):
        """
        头部添加节点
        :param item: 节点值
        :return:
        """
        node = Node(item)
        node.next = self.head
        self.head = node

    def append(self, item=20):
        """
        尾部添加节点
        :param items:
        :return:
        """
        cur = self.head
        if not cur:  # 判断是否为空链表
            self.add(item)
        else:
            node = Node(item)
            while cur.next:
                cur = cur.next
            cur.next = node

    @property
    def is_empty(self):
        """
        判断链表是否为空，只需要看头部是否有节点
        :return:
        """
        if self.head:
            return False
        else:
            return True

    @property
    def length(self):
        """
        获取链表长度
        :return:
        """
        cur = self.head
        n = 0
        if not cur:
            return n
        else:
            while cur.next:
                cur = cur.next
                n += 1
            return n+1

    def ergodic(self):
        """
        遍历链表
        :return:
        """
        cur = self.head
        if not cur:
            print('None')
        else:
            while cur.next:
                print(cur.item, end=' ')
                cur = cur.next
            print(cur.item, end='\n')

    def insert(self, index, item):
        """
        在指定位置插入节点(设置索引从0开始)
        :param item:
        :return:
        """
        if index == 0:  # 当索为0则头部插入
            self.add(item)
        elif index >= self.length:  # 当索引超范围则尾部插入
            self.append(item)
        else:  # 找到插入位置的上一个节点，修改上一个节点的next属性
            cur = self.head
            n = 1
            while cur.next:
                if n == index:
                    break
                cur = cur.next
                n += 1
            node = Node(item)
            node.next = cur.next
            cur.next = node

    def deltel(self, item):
        """
        删除节点
        :param item:
        :return:
        """
        if self.is_empty:  # 节点为空的情况
            raise ValueError("null")
        cur = self.head
        pre = None  # 记录删除节点的上一个节点
        if cur.item == item:  # 当删除节点为第一个的情况
            self.head = cur.next
        while cur.next:
            pre = cur
            cur = cur.next
            if cur.item == item:
                pre.next = cur.next

    def search(self, item):
        """
        查找节点是否存在
        :param item:
        :return:
        """
        cur = self.head
        while None != cur:
            if cur.item == item:
                return True
            cur = cur.next
        return False

    """
    没看懂
    """
    def removeNthFromEnd(self, n=2):
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.item = node.item
            return i
        index(self.head)
        return self.head.next



if __name__ == '__main__':
    lst = SinglyLinkedList()
    for i in range(10):
        lst.append(i)
    lst.ergodic()


    lst.removeNthFromEnd()


