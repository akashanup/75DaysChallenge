# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def merge(self, root1, root2, root):
        if root1 and root2:
            val = root1.val + root2.val
        elif root1:
            val = root1.val
        elif root2:
            val = root2.val
        else:
            return None
            
        root = TreeNode(val)
        root.left = self.merge(root1.left if root1 else None, root2.left if root2 else None, None)
        root.right = self.merge(root1.right if root1 else None, root2.right if root2 else None, None)

        return root
            
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is None:
            return root2
        if root2 is None:
            return root1
        return self.merge(root1, root2, None)
