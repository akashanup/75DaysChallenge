
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def dfs(self, node, hashmap):
        if not node:
            return None
        if node.val in hashmap:
            return hashmap[node.val]
        
        copy = Node(node.val)
        hashmap[node.val] = copy
        for neighbor in node.neighbors:
            copy.neighbors.append(self.dfs(neighbor, hashmap))
        return copy
    
    def cloneGraph(self, node: 'Node') -> 'Node':
        return self.dfs(node, {})
