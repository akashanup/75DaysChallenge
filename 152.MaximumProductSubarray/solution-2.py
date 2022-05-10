class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        numsRev = nums[::-1]

        for i in range(1, len(nums)):
            nums[i] *= nums[i-1] if nums[i-1] != 0 else 1
            numsRev[i] *= numsRev[i-1] if numsRev[i-1] != 0 else 1

        return max(nums+numsRev)
