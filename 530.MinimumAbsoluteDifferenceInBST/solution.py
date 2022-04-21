# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        minDiff = sys.maxsize
        pre = None
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return minDiff
            root = stack.pop()
            if pre:
                minDiff = min(minDiff, abs(pre.val-root.val))
            pre = root
            root = root.right
