# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        size = 0
        slow, fast = head, head
        while fast and fast.next:
            size += 1
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            slow = slow.next        
        
        node = head
        sentinel = ListNode()
        while size:
            nextNode = sentinel.next
            sentinel.next = node
            node = node.next
            sentinel.next.next = nextNode
            size -= 1
        
        node = sentinel.next
        while node and slow:
            if node.val != slow.val:
                return False
            node = node.next
            slow = slow.next
        
        return not node and not slow
