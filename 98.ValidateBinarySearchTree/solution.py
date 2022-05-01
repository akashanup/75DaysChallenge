# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createTrees(self, start, end):
        if start > end:
            return [None]
        trees = []
        '''
            For each i in [1-n], make i as the root, generate all possible left and right subtrees and then multiply them to get all the BSTs.
        '''
        for rootVal in range(start, end+1):
            leftSubtrees = self.createTrees(start, rootVal-1)
            rightSubtrees = self.createTrees(rootVal+1, end)
            for leftSubtree in leftSubtrees:
                for rightSubtree in rightSubtrees:
                    root = TreeNode(rootVal)
                    root.left = leftSubtree
                    root.right = rightSubtree
                    trees.append(root)
        return trees

    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        return self.createTrees(1, n)
