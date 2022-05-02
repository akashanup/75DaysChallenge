import heapq


class MedianFinder:
    def __init__(self):
        """
            At any point of time,
            1. If numbers are of even length then, low and high will be of length n and n
            2. If numbers are of odd length then, low will be of length n+1 and high will be of length n
        """
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, (-1) * num)
        heapq.heappush(self.high, (-1) * heapq.heappop(self.low))
        if len(self.low) < len(self.high):
            heapq.heappush(self.low, (-1) * heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) != len(self.high):
            return float((-1) * self.low[0])
        else:
            return round((self.high[0] - self.low[0]) / 2, 5)



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
