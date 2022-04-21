# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
            Using the property of BST that if the values of the given nodes are greater than root then it must be present in right subtree or else if the values are less than root then it must be present in left subtree.
            If any of the value is equal to the root then that root must be the LCA of the given two nodes.
        """
        while True:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root
