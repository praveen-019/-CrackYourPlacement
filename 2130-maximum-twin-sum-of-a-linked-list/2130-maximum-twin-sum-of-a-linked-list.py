# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        l = []
        while head is not None:
            l.append(head.val)
            head = head.next
        n = len(l)
        m = n//2
        res = 0
        for i in range(m):
            temp = l[i] + l[n-1-i]
            if temp > res:
                res = temp
        return res