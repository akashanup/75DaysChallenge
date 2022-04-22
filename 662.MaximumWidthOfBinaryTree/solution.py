# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        prevLevel, prevNum, maxWidth = 1, 1, 0
        queue = deque([[prevNum,prevLevel,root]])

        while queue:
            [num, level, node] = queue.popleft()
            if level > prevLevel:
                prevLevel, prevNum = level, num

            maxWidth = max(maxWidth, num - prevNum + 1)
            if node.left:
                queue.append([num*2,  level+1, node.left])
            if node.right:
                queue.append([num*2+1,level+1, node.right])

        return maxWidth
