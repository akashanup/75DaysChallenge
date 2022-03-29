class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minDiff = sys.maxsize
        threeSum = None
        for i in range(len(nums)):
            start, end = i+1, len(nums)-1
            while start < end:
                currSum = nums[i]+nums[start]+nums[end]
                if abs(target-currSum) < minDiff:
                    minDiff = abs(target-currSum)
                    threeSum = currSum
                if target == currSum:
                    return target
                else:
                    if target > currSum:
                        start += 1
                    else:
                        end -= 1
        return threeSum
