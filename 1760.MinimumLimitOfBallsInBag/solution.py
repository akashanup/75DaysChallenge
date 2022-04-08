"""
    Logic: This question is very similar to https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/discuss/1926040/python-binary-search-simple-solution-with-explanation
    Here, instead of capacity of the conveyor, we can apply the binary search on the size of bags as,
        1. minimum size of a bag could be 1
        2. maximum size of a bag could be max(nums)
    We now need to have an optimal size of bag which could accommodate the maxOperations on given nums.
    Now to check whether a size is valid to accommodate the maxOperations-
    This is calculated in isValid() function.
    The number of operations required for each bag to accommodate maxSize is calculated as num / maxsize.
    [NOTE] if a bag size is a multiple of num then we have to subtract 1 from operations because in this case remainder will be 0.
    Then if the sum of all operations is less than or equal to maxOperations then it is a valid bag size.
"""


class Solution:
    def isValid(self, nums, maxSize, maxOperations):
        requiredOperations = 0
        for num in nums:
            operation = num // maxSize
            if num % maxSize == 0:
                operation -= 1
            requiredOperations += operation
        return requiredOperations <= maxOperations

    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        minPenalty, maxPenalty = 1, max(nums)
        while minPenalty < maxPenalty:
            mid = minPenalty + ((maxPenalty-minPenalty)//2)
            if self.isValid(nums, mid, maxOperations):
                maxPenalty = mid
            else:
                minPenalty = mid+1
        return maxPenalty
