class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        if n <= 1:
            return n
        j = 0
        for i in range(n-1):
            if nums[i] != nums[i+1]:
                nums[j] = nums[i]
                j += 1
        nums[j] = nums[n-1]
        # All the values after index j can be removed.
        return j+1
