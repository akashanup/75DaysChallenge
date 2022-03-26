class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)

        prevSum = 0
        for i in range(len(nums)):
            if total == 2*prevSum + nums[i]:
                return i
            prevSum += nums[i]

        return -1
