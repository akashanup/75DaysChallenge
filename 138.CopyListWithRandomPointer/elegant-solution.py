# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Add the copied node without random pointer just after its corresponding original node.
        node = head
        while node:
            copiedNode = Node(node.val, node.next)
            node.next = copiedNode
            node = copiedNode.next

        """
            Update the random pointer of each copied node by using the below logic-
                Let's say the copied node is c_node and it's original node is o_node then the random pointer of c_node would be the next node of random pointer of o_node because we have placed each copied node just after it's original node. 
        """
        node = head
        while node:
            copiedNode = node.next
            if node.random:
                copiedNode.random = node.random.next
            node = copiedNode.next

        # Now just remove the original nodes from the list and return the remaining list as the remaining nodes of the list would make the deep copied list of original list.
        copiedHead = head.next
        node = head
        while node:
            copiedNode = node.next
            node.next = copiedNode.next
            node = node.next
            if copiedNode.next:
                copiedNode.next = copiedNode.next.next
                copiedNode = copiedNode.next
        return copiedHead
