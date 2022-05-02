import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-i for i in nums]
        heapq.heapify(heap)
        largestElements = []
        for i in range(k):
            largestElements.append(-heapq.heappop(heap))
        return largestElements[-1]
