# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        size = 0
        fast = head
        while fast and fast.next:
            size += 1
            fast = fast.next.next

        if fast:
            size = size*2 + 1
        else:
            size *= 2

        sentinel = ListNode()
        groupEnd = sentinel
        node = head
        for i in range(size//k):
            temp = groupEnd
            updateGroupEnd = False
            for j in range(k):
                nextNode = temp.next
                temp.next = node
                node = node.next
                temp.next.next = nextNode
                if not updateGroupEnd:
                    groupEnd = groupEnd.next
                    updateGroupEnd = True

        if groupEnd:
            groupEnd.next = node

        return sentinel.next
