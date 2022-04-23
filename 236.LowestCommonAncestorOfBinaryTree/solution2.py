"""
Assume p or q or both are not present in list.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findPath(self, root, node, path):
        if not root:
            return False
        path.append(root.val)
        if root.val == node:
            return True
        if (root.left and self.findPath(root.left, node, path)) or (root.right and self.findPath(root.right, node, path)):
            return True
        path.pop()
        return False

    def lowestCommonAncestor(self, root, p, q):
        pathP = []
        pathQ = []
        if (not self.findPath(root, p.val, pathP)) or (not self.findPath(root, q.val, pathQ)):
            return - 1
        i = 0
        while i < len(pathP) and i < len(pathQ):
            if pathP[i] != pathQ[i]:
                break
            i += 1
        return pathP[i - 1]
