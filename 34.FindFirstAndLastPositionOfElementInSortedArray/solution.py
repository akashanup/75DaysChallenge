class Solution:
    def left(self, nums, target):
        start = 0
        end = len(nums)
        while start < end:
            mid = start + ((end-start)//2)
            if nums[mid] < target:
                start = mid+1
            else:
                end = mid
        return start

    def right(self, nums, target):
        start = 0
        end = len(nums)
        while start < end:
            mid = start + ((end-start)//2)
            if target < nums[mid]:
                end = mid
            else:
                start = mid+1
        return start

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        start, end = self.left(nums, target), self.right(nums, target)-1
        if start == len(nums) or nums[start] != target:
            return [-1, -1]
        return [start, end]
