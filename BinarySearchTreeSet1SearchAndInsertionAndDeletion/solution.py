class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class Solution:
    def search(self, root, key):
        if root is None or root.val == key:
            return root
        if root.val < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if root.val == key:
                return root
            elif root.val < key:
                root.right = self.insert(root.right, key)
            else:
                root.left = self.insert(root.left, key)
        return root

    def minValueNode(self, root):
        while root.left:
            root = root.left
        return root

    def deleteNode(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.deleteNode(root.left, key)
        elif key > root.key:
            root.right = self.deleteNode(root.right, key)
        else:
            # Node found.
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left

            # Node with two children:
            # Get the inorder successor
            temp = self.minValueNode(root.right)

            # Copy the inorder successor's
            # content to this node
            root.key = temp.key

            # Delete the inorder successor
            root.right = self.deleteNode(root.right, temp.key)

        return root

    def ceil(self, root, key):
        if not root:
            return -1
        if root.key == key:
            return root.key

        # If root's key is smaller, ceil must be in right subtree
        if root.key < key:
            return self.ceil(root.right, key)

        # Else, either left subtree or root has the ceil value
        val = self.ceil(root.left, key)
        return val if val >= key else root.key

    def floor(self, root, key):
        if not root:
            return -1
        if root.key == key:
            return root.key

        # If root's key is larger, floor must be in left subtree
        if root.key > key:
            return self.ceil(root.left, key)

        # Else, either right subtree or root has the floor value
        val = self.ceil(root.right, key)
        return val if val <= key else root.key

