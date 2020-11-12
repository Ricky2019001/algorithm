# Definition for singly-linked list.
from leetcode.test_list.Single_list import *

class Solution:
    def reverse(self, head: SinglyLinkedList) -> SinglyLinkedList:
        pre = SinglyLinkedList()
        cur = head
        pre.next = cur
        if head == None or head.next == None:
            return None
        # 翻转
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        print(pre.item)
        return pre

    def isPalindrome(self, head: SinglyLinkedList) -> bool:
        pre = Node(0)
        cur = head
        tmp = head
        pre.next = cur
        if head == None or head.next == None:
            return True
        # 翻转
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp

        print()

        # pre
        while tmp:
            print(tmp.item, pre.item)
            if tmp.item != pre.item:
                return False
            tmp = tmp.next
            pre = pre.next
        return True


if __name__ == '__main__':
    lst = SinglyLinkedList()
    arr = [1,2]
    for i in range(len(arr)):
        lst.append(arr[i])
    lst.ergodic()

    res = Solution()
    res.reverse(lst.head)
    #print(res.isPalindrome(lst.head))

    # slt.isPalindrome()


