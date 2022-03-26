class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hashtable to track the seen numbers in array in the form of {num:index}
        seen = {}
        for i in range(len(nums)):
            counterPart = target - nums[i]
            if counterPart in seen:
                return [i, seen[counterPart]]
            seen[nums[i]] = i
