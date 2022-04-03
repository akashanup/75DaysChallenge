class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if min(nums) > 0 or n == 1:
            return True
        if nums[0] == 0:
            return False
        farthest = nums[0]
        current = nums[0]
        for num in range(1, n):
            if num == n-1:
                return True
            current -= 1
            farthest -= 1
            if farthest < nums[num]:
                farthest = nums[num]
            if current == 0:
                current = farthest
            if farthest == 0:
                return False
