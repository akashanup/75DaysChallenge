# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        li = []
        heapq.heapify(li)
        for i in range(len(lists)):
            h = lists[i]
            while h != None:
                heapq.heappush(li, h.val)
                h = h.next
        head = ListNode(-1, None)
        temp = head
        for i in range(len(li)):
            temp.next = ListNode(heapq.heappop(li))
            temp = temp.next
        return head.next
