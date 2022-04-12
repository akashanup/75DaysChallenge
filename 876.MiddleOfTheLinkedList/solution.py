# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Count the number of nodes i.e, Calculate the length of linked list
        tempHead = head
        listLen = 0
        while tempHead:
            listLen += 1
            tempHead = tempHead.next
        
        # Divide the length by 2 and move to that many nodes
        listLen //= 2
        while listLen > 0:
            listLen -= 1
            head = head.next
        return head
