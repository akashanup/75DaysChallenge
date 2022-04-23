# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root:
            levelNodes = {}
            queue = deque([[0, root]])
            while queue:
                currLevel, currNode = queue.popleft()
                if currLevel in levelNodes:
                    levelNodes[currLevel].append(currNode.val)
                else:
                    levelNodes[currLevel] = [currNode.val]
                if currNode.left:
                    queue.append([currLevel+1, currNode.left])
                if currNode.right:
                    queue.append([currLevel+1, currNode.right])
            rightView = []
            for level in levelNodes:
                rightView.append(levelNodes[level][-1])
            return rightView
        return []
