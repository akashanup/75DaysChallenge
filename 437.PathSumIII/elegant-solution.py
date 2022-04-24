"""
Logic:
    This problem is similar to the problem of finding the number of subarrays having a given sum k. Therefore, I will be using a similar logic like in [560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/discuss/1567849/Python-or-Prefix-Sum-Beats-99-or-Simplest-and-Efficient-Solution-With-Explanation)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.result = None
        self.lookup = None

    def pathSum(self, root, target):
        self.result = 0

        self.lookup = {}

        # recursive to get result
        self.dfs(root, target, 0)

        # return result
        return self.result

    def dfs(self, root, target, currSum):
        if not root:
            return None

        currSum = currSum + root.val

        if currSum == target:
            self.result += 1

        if (currSum - target) in self.lookup:
            self.result += self.lookup[currSum - target]

        if currSum in self.lookup:
            self.lookup[currSum] += 1
        else:
            self.lookup[currSum] = 1

        self.dfs(root.left, target, currSum)
        self.dfs(root.right, target, currSum)

        # Since path always has to be downwards and can't extend from left subtree to right subtree therefore, for every root node, the currentSum has to be decremented by 1.
        self.lookup[currSum] -= 1
