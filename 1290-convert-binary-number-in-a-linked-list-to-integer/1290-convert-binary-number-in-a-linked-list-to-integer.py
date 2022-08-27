# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l = []
        while head is not None:
            l.append(head.val)
            head = head.next
        n = len(l)
        res = 0
        for i in range(n):
            temp = l[i]*(2**(n-1-i))
            res += temp
        return res