# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = head.next
        temp = 0
        newHead = 0
        tail = 0
        while head is not None:
            if head.val == 0:
                if newHead == 0:
                    newNode = ListNode(temp)
                    newHead = newNode
                    tail = newNode
                else:
                    newNode = ListNode(temp)
                    tail.next = newNode
                    tail = newNode
                temp = 0
            else:
                temp += head.val
            head = head.next
        return newHead