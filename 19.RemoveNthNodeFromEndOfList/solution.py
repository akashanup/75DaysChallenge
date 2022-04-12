# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
            Let's the the number of nodes in linkedlist are sz then,
            nth node from end means (sz-n+1)th node from beginning.
        """
        # Calculate number of nodes in linkedlist
        halfSz = 1
        slow = fast = head
        while fast and fast.next:
            halfSz += 1
            slow = slow.next
            fast = fast.next.next

        """
            Since halfSz will denote the (number of nodes) // 2 or ((number of nodes) // 2) + 1.
            So calculate the total number of nodes accordingly based on odd or even value of halfSz.
            Now how to check whether the number of nodes are odd or even. This can be determined by fast pointer. 
            If fast is None then even number of nodes else odd number of nodes
        """
        if fast:
            #Odd
            sz = (2 * (halfSz-1)) + 1
        else:
            #Even
            sz = 2 * (halfSz - 1)

        # Check nth node from beginning lies in first half of second half of linked list
        if sz-n > halfSz:
            # Second half
            prev = None
            for i in range(halfSz, sz-n+1):
                prev = slow
                slow = slow.next
            prev.next = slow.next
            slow.next = None
        else:
            # First half
            prev = None
            tempHead = head
            for i in range(1, sz-n+1):
                prev = tempHead
                tempHead = tempHead.next

            if not prev:
                prev = head
                head = head.next
                prev.next = None
            else:
                prev.next = tempHead.next
                tempHead.next = None
        return head
