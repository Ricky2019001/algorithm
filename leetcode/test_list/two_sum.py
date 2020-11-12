# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dumpy = ListNode(0)
        cur = dumpy
        carry = 0
        while l1 or l2:
            lst1=l1 if l1 else None
            lst2=l2 if l2 else None
            s = lst1.val + lst2.val + carry
            carry = 1 if s > 9 else 0
            node = ListNode(s // 10)
            cur.next = node
            cur = cur.next
        if carry == 1:
            cur.next = ListNode(carry)
        return dumpy.next
