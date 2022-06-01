import heapq


class Solution:
    def __init__(self):
        # Since Python only supports min heaps therefore,
        # maxHeap will have values of first half of array and all the values will be negative because by that only we can find the maximum value of first half of array.
        self.maxHeap = []
        # minHeap will have values of second half of array and all the values will be positive because by that only we can find the minimum value of second half of array.
        self.minHeap = []

    def rebalanceHeaps(self):
        # If k is odd then maxHeap will have one extra element than minHeap. Else both will have same.
        while len(self.maxHeap) - len(self.minHeap) > 1:
            heapq.heappush(self.minHeap, -heapq.heappop(self.maxHeap))

        while len(self.maxHeap) < len(self.minHeap):
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))

    def addNum(self, num):
        if not self.maxHeap or -self.maxHeap[0] > num:
            # Since we first negate the number and then store it, therefore, it will always pop out the largest number present in heap.
            heapq.heappush(self.maxHeap, -num)
        else:
            # Since we first negate the number that is popped out from max heap which means that the number eventually becomes positive again and then store it, therefore, it will always pop out the smallest number present in heap.
            heapq.heappush(self.minHeap, num)
        self.rebalanceHeaps()

    def removeNum(self, num):
        if num > -self.maxHeap[0]:
            self.minHeap.remove(num)
            heapq.heapify(self.minHeap)
        else:
            self.maxHeap.remove(-num)
            heapq.heapify(self.maxHeap)
        self.rebalanceHeaps()

    def getCurrentMedian(self):
        if len(self.maxHeap) != len(self.minHeap):
            median = round(-self.maxHeap[0], 5)
        else:
            median = round((self.minHeap[0] - self.maxHeap[0]) / 2, 5)
        return median

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        medians = [None] * (len(nums)-k+1)
        j = 0

        for i in range(len(nums)):
            if i >= k:
                # Remove nums[i-k] from appropriate heap
                self.removeNum(nums[i-k])

            # addNum(self.nums[i])
            self.addNum(nums[i])

            if i >= k-1:
                # getCurrentMedian()
                medians[j] = self.getCurrentMedian()
                j += 1

        return medians
