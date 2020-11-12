# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def kthToLast(self, head: ListNode, k: int) -> int:
        if k < 0:
            return -1
        if head is None:
            return -1
        cnt = 0
        cur = head
        res = head
        while cur:
            cnt += 1
            if cnt == k:
                res = res.next
            cur = cur.next
        return res.val