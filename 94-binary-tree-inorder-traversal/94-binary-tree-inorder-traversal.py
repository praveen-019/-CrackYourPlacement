# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def printTree(root,l):
            if root is None:
                return
            printTree(root.left,l)
            l.append(root.val)
            printTree(root.right,l)
        l = []
        printTree(root,l)
        return l