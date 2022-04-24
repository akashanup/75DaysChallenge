# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, lookup):
        if not root:
            return []
        lookup[root] = [root.val]
        for val in self.dfs(root.left, lookup):
            lookup[root].append(root.val + val)
        for val in self.dfs(root.right, lookup):
            lookup[root].append(root.val + val)
        return lookup[root]

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        lookup = {}
        # For each node lets calculate the sum of values of possible paths.
        self.dfs(root, lookup)
        count = 0
        # Now for each node, check the number of values == targetSum will be the number of of options for that node.
        for node in lookup:
            for value in lookup[node]:
                if value == targetSum:
                    count += 1
        return count
