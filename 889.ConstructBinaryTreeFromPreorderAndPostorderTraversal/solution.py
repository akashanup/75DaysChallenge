# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not postorder:
            return None
        root = TreeNode(preorder[0])
        if len(postorder) == 1:
            return root

        rightSubTreeIndex = preorder.index(postorder[-2])
        root.left = self.constructFromPrePost(preorder[1: rightSubTreeIndex], postorder[:(rightSubTreeIndex - 1)])
        root.right = self.constructFromPrePost(preorder[rightSubTreeIndex: ], postorder[(rightSubTreeIndex - 1):-1])
        return root

