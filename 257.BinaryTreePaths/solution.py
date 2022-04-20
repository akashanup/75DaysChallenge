import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        heap = [[-val, key] for key,val in hashmap.items()]
        heapq.heapify(heap)

        frequent = [None] * k
        for i in range(k):
            frequent[i] = heapq.heappop(heap)[1]

        return frequent

