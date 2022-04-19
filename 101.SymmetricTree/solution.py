# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirrorImage(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            exterior = self.isMirrorImage(left.left, right.right)
            interior = self.isMirrorImage(left.right, right.left)
            return exterior and interior
        return False
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isMirrorImage(root.left, root.right)
