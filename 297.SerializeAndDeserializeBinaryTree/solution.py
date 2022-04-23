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

        def dfs(root):
            if not root:
                ans.append('#')
                return
            ans.append(str(root.val))
            dfs(root.left)
            dfs(root.right)

        ans = []
        dfs(root)
        return ' '.join(ans)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def dfs(index):
            if data[index] == '#': return None, index
            root = TreeNode(int(data[index]))
            root.left, index = dfs(index + 1)
            root.right, index = dfs(index + 1)
            return root, index

        data = data.split()
        return dfs(0)[0]

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))

