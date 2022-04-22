# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def dfs(self, root, maxVal=-sys.maxsize):
        if root:
            if root.val >= maxVal:
                return 1 + self.dfs(root.left, root.val) + self.dfs(root.right, root.val)
            return self.dfs(root.left, maxVal) + self.dfs(root.right, maxVal)
        return 0

    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root)
        '''
            Or We can solve via BFS also
            queue = [[root, -sys.maxsize]]
            good = 0
            while queue:
                current = queue.pop(0)
                maxVal = current[1]
                if current[0].val >= maxVal:
                    good += 1
                    maxVal = current[0].val
                if current[0].left:
                    queue.append([current[0].left, maxVal])
                if current[0].right:
                    queue.append([current[0].right, maxVal])
            return good
        '''
