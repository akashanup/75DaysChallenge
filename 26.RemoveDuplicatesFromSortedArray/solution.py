class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        i = 1
        dupStart, dupEnd = None, None
        while i < len(nums):
            if nums[i] == nums[i-1]:
                # Duplicate Found
                if dupEnd is None:
                    dupStart = dupEnd = i
                else:
                    dupEnd = i
            else:
                while i < len(nums)-1 and nums[i] == nums[i+1]:
                    # Duplicate Found
                    if not dupStart:
                        dupStart = i
                    dupEnd = i
                    i += 1

                if dupStart is not None:
                    # Swap the current element with the element at index dupStart
                    nums[dupStart], nums[i] = nums[i], nums[dupStart]
                    dupStart += 1
            i += 1

        return dupStart if dupStart else len(nums)
