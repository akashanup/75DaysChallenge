# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
            Since inorder traversal of BST gives a sorted array so if inorder traversal of given BST is not sorted then it is not a valid BST.
        """
        pre = None
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return True
            root = stack.pop()
            if pre and pre.val >= root.val:
                return False
            pre = root
            root = root.right
