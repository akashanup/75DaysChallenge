# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.push(root)
    
    def push(self, root):
        node = root
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        minimum = self.stack.pop()
        self.push(minimum.right)
        return minimum.val

    def hasNext(self) -> bool:
        return self.stack


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
