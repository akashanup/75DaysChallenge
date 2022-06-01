from sortedcontainers import SortedList


class Solution:
    def calcMedian(self, nums):
        if len(nums) & 1:
            return round(nums[len(nums)//2], 5)
        else:
            mid = len(nums)//2
            return round((nums[mid] + nums[mid-1]) / 2, 5)

    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        medians = [None] * (len(nums)-k+1)
        j = 0

        sortedList = SortedList()

        for i in range(len(nums)):
            if i >= k:
                # Remove nums[i-k] from sortedList. O(logK)
                sortedList.remove(nums[i-k])

            # O(logK)
            sortedList.add(nums[i])

            if i >= k-1:
                medians[j] = self.calcMedian(sortedList)
                j += 1

        return medians

