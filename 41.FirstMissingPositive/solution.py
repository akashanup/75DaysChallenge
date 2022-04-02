class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        # Cyclic Sort by ignoring numbers which are less then 1 or greater than or equalt to length of array. This is done because cyclic sort sorts an array in o(n) iff numbers are in a proper range.
        while i < len(nums):
            correct = nums[i] - 1
            if nums[i] <= 0 or nums[i] > len(nums) or nums[i] == nums[correct]:
                i += 1
            else:
                nums[i], nums[correct] = nums[correct], nums[i]
                
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums) + 1