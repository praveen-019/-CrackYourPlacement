# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import queue
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = 0
        q = queue.Queue()
        if root is not None:
            q.put(root)
        while (not(q.empty())):
            currNode = q.get()
            if currNode.val >= low and currNode.val <= high:
                res += currNode.val
            if currNode.left is not None:
                q.put(currNode.left)
            if currNode.right is not None:
                q.put(currNode.right)
        return res