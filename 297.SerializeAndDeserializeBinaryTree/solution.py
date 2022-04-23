# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '#'
        return '|'.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])

    def createTree(self, data, i):
        if data[i] == '#':
            return None, i
        root = TreeNode(data[i])
        root.left, i = self.createTree(data, i + 1)
        root.right, i = self.createTree(data, i + 1)
        return root, i

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        return self.createTree(data.split('|'), 0)[0]

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
