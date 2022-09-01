# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import queue
class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = queue.Queue()
        q.put(cloned)
        while (not(q.empty())):
            curr = q.get()
            if curr.val == target.val:
                return curr
            if curr.left is not None:
                q.put(curr.left)
            if curr.right is not None:
                q.put(curr.right)