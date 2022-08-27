# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fastHead = head
        slowHead = head
        prev = head
        while fastHead.next is not None:
            if fastHead.next.next is None:
                if slowHead != head:
                    prev = prev.next
                fastHead = fastHead.next
                slowHead = slowHead.next
            else:
                if slowHead != head:
                    prev = prev.next
                fastHead = fastHead.next.next
                slowHead = slowHead.next
        if head.next == None:
            return None
        prev.next = slowHead.next
        return head