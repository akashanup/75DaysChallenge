import heapq


class Solution:
    def sortNearlySortedArrays(self, arr, k):
        heap = arr[:k + 1]
        heapq.heapify(heap)
        minValIdx = 0
        for remainingIdx in range(k + 1, len(arr)):
            arr[minValIdx] = heapq.heappop(heap)
            heapq.heappush(heap, arr[remainingIdx])
            minValIdx += 1

        while heap:
            arr[minValIdx] = heapq.heappop(heap)
            minValIdx += 1

        return arr


print(Solution().sortNearlySortedArrays([6, 5, 3, 2, 8, 10, 9], 3))
