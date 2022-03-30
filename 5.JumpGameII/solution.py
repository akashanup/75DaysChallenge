class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1 or nums[0] == 0:
            return 0

        current = farthest = nums[0]
        steps = 1
        i = 1
        while i < len(nums)-1:
            current -= 1
            farthest -= 1
            farthest = max(farthest, nums[i])
            if current == 0:
                steps += 1
                current = farthest
            i += 1
        return steps
