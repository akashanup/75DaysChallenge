# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode], reversedLinkedList=None) -> Optional[ListNode]:
        if not head:
            return reversedLinkedList
        next = head.next
        head.next = reversedLinkedList
        return self.reverseList(next, head)
