# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        res = head
        a = head.val
        b = head
        head = head.next
        while head is not None:
            if head.val != a:
                b.next = head
                a = head.val
                b = head
            head = head.next
        b.next = None
        return res
                