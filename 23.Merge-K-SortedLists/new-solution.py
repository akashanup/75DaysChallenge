# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, list1, list1tail, list2):
        if list2 is None:
            return list1, list1tail
        if list1tail and list1tail.val <= list2.val:
            while list2:
                list1tail.next = list2
                list1tail = list1tail.next
                list2 = list2.next
            return list1, list1tail
        else:
            if list1.val < list2.val:
                merged = list1
                list1 = list1.next
            else:
                merged = list2
                list2 = list2.next
            merged.next = None
            head = merged
            while list1 and list2:
                if list1.val < list2.val:
                    merged.next = list1
                    merged = merged.next
                    list1 = list1.next
                else:
                    merged.next = list2
                    merged = merged.next
                    list2 = list2.next
                merged.next = None
            while list1:
                merged.next = list1
                merged = merged.next
                list1 = list1.next
                merged.next = None
            while list2:
                merged.next = list2
                merged = merged.next
                list2 = list2.next
                merged.next = None
            return head, merged

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        i = 0
        while i < len(lists):
            if lists[i] is not None:
                break
            i += 1
        if i == len(lists):
            return None

        head = lists[i]
        tail = None
        for l in lists[i + 1:]:
            head, tail = self.merge(head, tail, l)
        return head
