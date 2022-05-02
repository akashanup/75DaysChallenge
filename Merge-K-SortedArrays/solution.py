import heapq


class Solution:
    def mergeKSortedArrays(self, arr):
        output = []
        heap = []
        arrIdx = [0] * len(arr)
        while True:
            for i in range(len(arrIdx)):
                if arrIdx[i] < len(arr[i]):
                    heapq.heappush(heap, arr[i][arrIdx[i]])
                    arrIdx[i] += 1
            if not heap:
                return output
            output.append(heapq.heappop(heap))


print(Solution().mergeKSortedArrays([[1, 3, 5, 7],  [2, 4, 6, 8], [0, 9, 10, 11]]))
