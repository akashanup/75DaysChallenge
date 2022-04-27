# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None or (root.left is None and root.right is None):
            return
        if root.left:
            self.flatten(root.left)
            rightTree = root.right
            root.right = root.left
            root.left = None
            while root.right:
                root = root.right
            root.right = rightTree
        if root.right:
            self.flatten(root.right)  
