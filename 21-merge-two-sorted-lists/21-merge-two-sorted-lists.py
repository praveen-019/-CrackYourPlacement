# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val < list2.val:
            finalHead = list1
            finalTail = list1
            list1 = list1.next
        else:
            finalHead = list2
            finalTail = list2
            list2 = list2.next
        
        while list1 != None and list2 != None:
            if(list1.val < list2.val):
                finalTail.next = list1
                finalTail = list1
                list1 = list1.next
            else:
                finalTail.next = list2
                finalTail = list2
                list2 = list2.next
        if(list1 != None):
            finalTail.next = list1
        else:
            finalTail.next = list2
        return finalHead