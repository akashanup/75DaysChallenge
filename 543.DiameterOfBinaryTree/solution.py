# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Calculate the height of a node.
    def height(self, node, nodeHeights):
        if node:
            if node not in nodeHeights:
                nodeHeights[node] = 1 + max(self.height(node.left, nodeHeights), self.height(node.right, nodeHeights))
            return nodeHeights[node]
        return 0

    # Calculate diameter of each node (considering as root)
    def calculateDiameter(self, root, diameter, nodeHeights):
        if root:
            diameter = max(diameter, self.height(root.left, nodeHeights) + self.height(root.right, nodeHeights))
            diameter = max(diameter, self.calculateDiameter(root.left, diameter, nodeHeights),
                           self.calculateDiameter(root.right, diameter, nodeHeights))
        return diameter

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        return self.calculateDiameter(root, 0, {})
