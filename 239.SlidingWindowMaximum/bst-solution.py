"""
Logic:
    For each window of size k, we will maintain an AVL tree and the maximum element for any window will be the rightmost node of AVl tree.
    Complexity of this solution would be O(n*LogK) as insertion, deletion and search operation of AVL tree takes logN time.
    There is an even more optimised solution(Solution 2) in which we use deque and reduce the complexity to O(n).
"""


class TreeNode:
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1


# AVL Tree
class BalancesBST:
    def getTreeNode(self, val):
        return TreeNode(val)

    def getHeight(self, root):
        if not root:
            return 0
        return root.height

    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def rotateLeft(self, root):
        if not root.right:
            return root
        right = root.right
        t2 = right.left

        # Perform Rotation
        right.left = root
        root.right = t2

        # Update heights
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        right.height = 1 + max(self.getHeight(right.left), self.getHeight(right.right))

        # Return new root
        return right

    def rotateRight(self, root):
        if not root.left:
            return root
        left = root.left
        t3 = left.right

        # Perform Rotation
        left.right = root
        root.left = t3

        # Update heights
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        left.height = 1 + max(self.getHeight(left.left), self.getHeight(left.right))

        # Return new root
        return left

    # Recursive function to insert key in subtree rooted with node and returns new root of subtree.
    def insert(self, root, val):
        # Step 1 - Perform normal BST
        if not root:
            return self.getTreeNode(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        # Step 2 - Update the height of the ancestor node.
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced, then try out the 4 cases-
        # Case 1 - Left-Left
        if balance > 1 and val < root.left.val:
            return self.rotateRight(root)
        # Case 2 - Right-Right
        if balance < -1 and val > root.right.val:
            return self.rotateLeft(root)
        # Case 3 - Left-Right
        if balance > 1 and val > root.left.val:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        # Case 4 - Right-Left
        if balance < -1 and val < root.right.val:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root

        return self.getMinValueNode(root.left)

    # Recursive function to delete key in subtree rooted with node and returns new root of subtree.
    def delete(self, root, val):
        # Step 1 - Perform normal BST
        if not root:
            return root
        elif val < root.val:
            root.left = self.delete(root.left, val)
        elif val > root.val:
            root.right = self.delete(root.right, val)
        else:
            # Remove root
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            else:
                temp = self.getMinValueNode(root.right)
                root.val = temp.val
                root.right = self.delete(root.right, temp.val)

        # If the tree has only one node, simply return it.
        if root is None:
            return root

        # Step 2 - Update the height of the ancestor node.
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # Step 3 - Get the balance factor
        balance = self.getBalance(root)

        # Step 4 - If the node is unbalanced, then try out the 4 cases-
        # Case 1 - Left-Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rotateRight(root)
        # Case 2 - Right-Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.rotateLeft(root)
        # Case 3 - Left-Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.rotateLeft(root.left)
            return self.rotateRight(root)
        # Case 4 - Right-Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rotateRight(root.right)
            return self.rotateLeft(root)

        return root

    def getMax(self, root):
        node = root
        while node.right:
            node = node.right
        return node.val

    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.val)
            self.inorder(root.right)


class Solution:
    def maxSlidingWindow(self, nums, k):
        maxWindow = [None]*(len(nums)-k+1)
        root = None
        avl = BalancesBST()
        i = 0
        while i < len(nums):
            root = avl.insert(root, nums[i])
            if i >= k-1:
                # Got a new window of size k. Find maximum and remove the first element of window.
                maxWindow[i-k+1] = avl.getMax(root)
                root = avl.delete(root, nums[i-k+1])
            i += 1
        return maxWindow


print(Solution().maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], k=3))
# [3,3,5,5,6,7]
