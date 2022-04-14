# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getNodeResponsibleForCycle(self, head, nodeInCycle):
        # Calculate size of cycle
        size = 1
        node = nodeInCycle
        while node.next != nodeInCycle:
            size += 1
            node = node.next

        node1, node2 = head, head
        while size > 0:
            node2 = node2.next
            size -= 1

        while node1 != node2:
            node1 = node1.next
            node2 = node2.next

        return node1

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # Cycle found!
                return self.getNodeResponsibleForCycle(head, slow)
        # No cycle!
        return None
