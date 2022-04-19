class DoublyLinkedListNode:
    def __init__(self, val=None, right=None, left=None):
        self.val = val
        self.right = right
        self.left = left


class LRUCache:

    def __init__(self, capacity: int):
        self.nodes = {}
        self.start = None
        self.end = None
        self.capacity = capacity

    # Move the node to end of DLL
    def moveNodeToEnd(self, node):
        # Detach node. Detach iff there are more than 1 nodes and the node to be deatched isn't the last node.
        if self.start != self.end and self.end != node:
            leftNode = node.left
            node.left = None
            if leftNode:
                leftNode.right = node.right
            rightNode = node.right
            node.right = None
            rightNode.left = leftNode
            # If the detached node was the first node then update start to second node(rightNode).
            if self.start == node:
                self.start = rightNode

            # Add the node at the end
            self.end.right = node
            node.left = self.end
            self.end = node

    def get(self, key: int) -> int:
        if key in self.nodes:
            self.moveNodeToEnd(self.nodes[key][0])
            return self.nodes[key][1]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.nodes[key][1] = value
            self.moveNodeToEnd(self.nodes[key][0])
        else:
            if len(self.nodes) == self.capacity:
                # Evict the LRU node. It would always be the first node.
                lruKey = self.start.val
                if self.start == self.end:
                    self.start = None
                    self.end = None
                else:
                    secondNode = self.start.right
                    self.start.right = None
                    secondNode.left = None
                    self.start = secondNode

                # Delete it from hashmap too.
                del self.nodes[lruKey]

            # Add the new node at last.
            newNode = DoublyLinkedListNode(key)
            if not self.start:
                self.start = self.end = newNode
            else:
                self.end.right = newNode
                newNode.left = self.end
                self.end = newNode
            # Add the key in hashmap
            self.nodes[key] = [newNode, value]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
