# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        
        
        """
            1. Find the length of linkedlist.
            2. Pluck out last k nodes of linkedlist.
            3. Attach the plucked out nodes infront of the remaining linkedlist and return.
        """
        
        listLen = 0
        node = head
        lastNode = None
        while node:
            listLen += 1
            lastNode = node
            node = node.next
        
        k %= listLen
        if k == 0:
            return head
        
        i = 0
        node = head
        prevNode = None
        while i < listLen - k:
            i += 1
            prevNode = node
            node = node.next
        prevNode.next = None
        lastNode.next = head
        return node
