# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        a = l1
        b = l2
        c1 = 1
        c2 = 1
        while a.next is not None:
            c1 += 1
            a = a.next
        while b.next is not None:
            c2 += 1
            b = b.next
        ex = 0
        head = None
        m = min(c1,c2)
        for i in range(m):
            temp = l1.val + l2.val + ex
            if temp <= 9:
                value = temp
                ex = 0
            else:
                value = temp%10
                ex = temp//10
            newNode = ListNode(value)
            if head == None:
                head = newNode
                tail = newNode
            else:
                tail.next = newNode
                tail = newNode
            l1 = l1.next
            l2 = l2.next
        if c1 > c2:
            for i in range(m,c1):
                temp = l1.val + ex
                if temp <= 9:
                    value = temp
                    ex = 0
                else:
                    value = temp%10
                    ex = temp//10
                newNode = ListNode(value)
                if head == None:
                    head = newNode
                    tail = newNode
                else:
                    tail.next = newNode
                    tail = newNode
                l1 = l1.next
        if c2 > c1:
            for i in range(m,c2):
                temp = l2.val + ex
                if temp <= 9:
                    value = temp
                    ex = 0
                else:
                    value = temp%10
                    ex = temp//10
                newNode = ListNode(value)
                if head == None:
                    head = newNode
                    tail = newNode
                else:
                    tail.next = newNode
                    tail = newNode
                l2 = l2.next
        if temp > 9:
            newNode = ListNode(ex)
            tail.next = newNode
            tail = newNode
        return head