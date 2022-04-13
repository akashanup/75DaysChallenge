# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1 = []
        stack2 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        sentinel = ListNode()
        carry = 0
        while stack1 and stack2:
            val = stack1.pop() + stack2.pop()
            nextNode = sentinel.next
            sentinel.next = ListNode((carry+val)%10)
            sentinel.next.next = nextNode
            carry = (carry+val) // 10

        while stack1:
            val = stack1.pop()
            nextNode = sentinel.next
            sentinel.next = ListNode((carry+val)%10)
            sentinel.next.next = nextNode
            carry = (carry+val) // 10

        while stack2:
            val = stack2.pop()
            nextNode = sentinel.next
            sentinel.next = ListNode((carry+val)%10)
            sentinel.next.next = nextNode
            carry = (carry+val) // 10

        if carry:
            nextNode = sentinel.next
            sentinel.next = ListNode(carry)
            sentinel.next.next = nextNode

        return sentinel.next
