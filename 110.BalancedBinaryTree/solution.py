# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self, root, lookup):
        if not root:
            return 0
        if root not in lookup:
            lookup[root] = 1 + max(self.height(root.left, lookup), self.height(root.right, lookup))
        return lookup[root]

    def isBalanced(self, root: Optional[TreeNode], lookup={}) -> bool:
        if not root or (not root.left and not root.right):
            return True
        if self.isBalanced(root.left, lookup) and self.isBalanced(root.right, lookup):
            return abs(self.height(root.left, lookup)-self.height(root.right, lookup)) <= 1
        return False
