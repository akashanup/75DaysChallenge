# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def compareSubTreeStructure(self, root, subRoot):
        if (root and not subRoot) or (subRoot and not root):
            return False
        if not root and not subRoot:
            return True
        return root.val == subRoot.val and (self.compareSubTreeStructure(root.right, subRoot.right)) and (self.compareSubTreeStructure(root.left, subRoot.left))

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root.val == subRoot.val:
            # Potential subtree found!
            if self.compareSubTreeStructure(root, subRoot):
                return True
        return (root.left and self.isSubtree(root.left, subRoot)) or (root.right and self.isSubtree(root.right, subRoot))
