class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []
        nums = sorted(nums)
        fourSumCount = {}
        for i in range(n-3):
            for j in range(i+1, n-2):
                initialSum = nums[i] + nums[j]
                left = j + 1
                right = n - 1
                while left < right:
                    if initialSum + nums[left] + nums[right] > target:
                        right -= 1
                    elif initialSum + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        if (nums[i], nums[j], nums[left], nums[right]) not in fourSumCount:
                            fourSumCount[(nums[i], nums[j], nums[left], nums[right])] = target
                        left += 1
                        right -= 1
        return [list(i) for i in fourSumCount.keys()]
