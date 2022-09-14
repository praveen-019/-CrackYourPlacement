'''class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
import queue
class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        q = queue.Queue()
        root = Node(n)
        q.put(root)
        while (not(q.empty())):
            curr = q.get()
            a = curr.data-1
            b = curr.data-2
            if a == 0:
                count += 1
            if b == 0:
                count += 1
            if a >= 0:
                left = Node(a)
                curr.left = left
                q.put(left)
            if b >= 0:
                right = Node(b)
                curr.right = right
                q.put(right)
        return count'''
    
class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1
        for i in range(n):
            one,two = two,one+two
        return one