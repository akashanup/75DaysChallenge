"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def dfs(self, root, parent):
        if root:
            root.next = parent
            # Next pointer of left child of current node will be the right child of the node
            self.dfs(root.left, root.right)
            # Next pointer of right child of current node will be the left child of the parent node
            self.dfs(root.right, parent.left if parent else None)
        return root
    
    def connect(self, root: 'Node') -> 'Node':
        return self.dfs(root, None)
