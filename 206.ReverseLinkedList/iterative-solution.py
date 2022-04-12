# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        # Sentinel Node
        reverse = ListNode()
        while head:
            node = reverse.next
            reverse.next = head
            head = head.next
            reverse.next.next = node

        return reverse.next
