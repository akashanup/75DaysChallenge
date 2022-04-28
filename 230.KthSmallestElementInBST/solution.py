# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.head, self.tail = None, None

    def createDLLFromBST(self, root):
        if root:
            self.createDLLFromBST(root.left)
            # Add node at the end of doubly linked list.
            right = root.right
            self.insertToDllAtLast(root)
            self.createDLLFromBST(right)

    def insertToDllAtLast(self, node):
        if not self.tail:
            # Add first node.
            self.head = self.tail = node
        else:
            node.left = self.tail
            self.tail.right = node
            self.tail = self.tail.right

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.createDLLFromBST(root)
        node = self.head
        i = 1
        while i < k:
            node = node.right
            i += 1
        return node.val
