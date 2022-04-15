"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        node = head
        while node:
            if node.child:
                nextNode = node.next
                child = self.flatten(node.child)
                child.prev = node
                node.next = child
                while child and child.next:
                    child = child.next
                child.next = nextNode
                if nextNode:
                    nextNode.prev = child
                node.child = None
                node = nextNode
            else:
                node = node.next
        return head
