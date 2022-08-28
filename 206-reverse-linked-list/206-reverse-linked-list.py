# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while head is not None:
            if curr == head:
                head = head.next
                curr.next = None
            else:
                temp = curr
                curr = head
                head = head.next
                curr.next = temp
        return curr