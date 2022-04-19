# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root):
        if root is None:
            return []
        levelOrderNodes = {}
        level = 0
        queue = [[level, root]]
        while len(queue):
            level, node = queue.pop(0)
            if level in levelOrderNodes:
                levelOrderNodes[level].append(node.val if node else None)
            else:
                levelOrderNodes[level] = [node.val if node else None]
            if node:
                queue.append([level+1, node.left])
                queue.append([level+1, node.right])
        return list(levelOrderNodes.values())

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = self.levelOrder(root.left)
        right = self.levelOrder(root.right)
        if len(left) != len(right):
            return False
        i = 0
        while i < len(left):
            if left[i] != right[i][::-1]:
                return False
            i += 1
        return True
        
