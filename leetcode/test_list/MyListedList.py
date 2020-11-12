class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = Node(-1)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0:
            return -1
        cur = self.head.next
        i = 0
        while cur:
            if i == index:
                return cur.val
            i += 1
            cur = cur.next

        return -1


    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        node = Node(val)
        if self.head.next == None:
            self.head.next = node
            node.next = None
        else:
            node.next = self.head.next
            self.head.next = node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        if self.head.next == None:
            self.head.next = node
            node.next = None
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.next = None

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        cur = self.head
        if index < 0:
            self.addAtHead(val)
        for _ in range(index):
            cur = cur.next
            if not cur:
                break
        node = Node(val)
        node.next = cur.next
        cur.next = node
        cur = node


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0:
            return
        cur = self.head
        for _ in range(index):
            if not cur.next:
                return
            cur = cur.next
        if cur.next and cur.next.next:
            cur.next = cur.next.next
        else:
            cur.next = None

    def traversal(self):
        cur = self.head.next
        while cur:
            print(cur.val, end=',')
            cur = cur.next
        print()


if __name__ == '__main__':
    obj = MyLinkedList()
    obj.addAtHead(1)
    obj.addAtHead(2)
    obj.addAtHead(3)
    obj.addAtHead(4)
    obj.addAtHead(5)
    obj.addAtHead(6)
    n=obj.get(3)
    print(n)
    obj.addAtTail(13)
    obj.addAtTail(14)
    obj.traversal()
    # obj.addAtIndex(1, 4)
    # obj.deleteAtIndex(2)