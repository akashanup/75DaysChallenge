class DoublyLinkedListNode:
    def __init__(self, val=None, head=None, tail=None):
        self.val = val
        self.head = head
        self.tail = tail


class LRUCache:

    def __init__(self, capacity: int):
        self.nodes = {}
        self.start = None
        self.end = None
        self.capacity = capacity

    # Move the node to start of DLL
    def moveNodeToStart(self, node):
        if self.start != node:
            previousNode = node.tail
            if previousNode:
                previousNode.head = node.head
                nextNode = node.head
                if nextNode:
                    nextNode.tail = previousNode
                else:
                    self.end = previousNode
                startingNode = self.start
                node.head = startingNode
                node.tail = None
                startingNode.tail = node
                self.start = node

    def get(self, key: int) -> int:
        if key not in self.nodes:
            return -1
        self.moveNodeToStart(self.nodes[key])
        return self.nodes[key].val[1]

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            self.nodes[key].val = [key, value]
            self.moveNodeToStart(self.nodes[key])
        else:
            if len(self.nodes) == self.capacity:
                # Evict the node at the end
                lastNode = self.end
                previousNode = lastNode.tail
                self.end = lastNode.tail
                lastNode.tail = None
                if previousNode:
                    previousNode.head = None
                del self.nodes[lastNode.val[0]]
            # Add new node in the start
            dllNode = DoublyLinkedListNode([key, value])
            startingNode = self.start
            dllNode.head = startingNode
            if startingNode:
                startingNode.tail = dllNode
            if self.end is None:
                self.end = dllNode
            self.start = dllNode
            self.nodes[key] = dllNode


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
