# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        """
        用一个变量pre_sum记录前缀和，
        再用一个哈希表记录出现过的前缀和，如果出现了两个相同的前缀和，就说明中间这一段的和为0。

        举例：
        对于输入 [1, 2, -2, 3, -1, -1, -1]，前缀和为[1, 3, 1, 4, 3, 2, 1]，下标为0的1和下标为2的1相同，就代表下标在         【1， 2】间的元素的和为0。
        """
        cur = head
        dummy = ListNode(-1)
        dummy.next = cur
        dict = {0: dummy}
        pre_sum = 0
        if not cur:
            return cur
        while cur:
            pre_sum += cur.val
            if pre_sum in dict:
                dict[pre_sum].next = cur.next if cur.next else None
                pre_sum = 0
            else:
                dict[pre_sum] = cur
            cur = cur.next

        return dummy.next
