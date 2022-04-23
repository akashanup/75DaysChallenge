# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getPath(self, root, target, path):
        if not root:
            return False
        if root.val == target.val:
            return True
        path.append(root)
        if self.getPath(root.left, target, path) or self.getPath(root.right, target, path):
            return True
        path.pop()
        return False
    
    def kDistantNodes(self, root, k):
        if not root:
            return []
        if k == 0:
            return [root.val]
        return self.kDistantNodes(root.left, k-1) + self.kDistantNodes(root.right, k-1)
    
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        if k == 0:
            return [target.val]
        path = []
        if not self.getPath(root, target, path):
            return []
        
        # Find all the nodes that are k distant from target node in its subtrees
        nodes = self.kDistantNodes(target, k)
        
        # Find all the nodes that are k-1 distant from its parent, k-2 distant from its grandparent and so on and so forth in opposite subtree
        currNode = target
        while path and k > 0:
            parent = path.pop()
            # Reduce k by 1 as we are referring to currNode's parent now
            k -= 1
            
            if k == 0:
                nodes += [parent.val]
            elif parent.left == currNode:
                # Reduce k by 1 as we are referring to currNode's parent's other child
                nodes += self.kDistantNodes(parent.right, k-1)
            else:
                # Reduce k by 1 as we are referring to currNode's parent's other child
                nodes += self.kDistantNodes(parent.left, k-1)
            
            currNode = parent
        
        return nodes
