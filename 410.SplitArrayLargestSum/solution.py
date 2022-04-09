class Solution:
    def countSubArrays(self, nums, maxSum):
        subArrays = 1
        numsSum = 0
        for num in nums:
            if numsSum + num <= maxSum:
                numsSum += num
            else:
                subArrays += 1
                numsSum = num
        return subArrays

    def splitArray(self, nums: List[int], m: int) -> int:
        """
            Let's say m = 1 then, the maximum sum of m sub-arrays would definitely be sum(nums) as there would be only one sub-array.
            Let's say m = len(nums) then, the maximum sum of m sub-arrays would definitely be max(nums) as there would be len(nums) sub-arrays of length 1 each.
            So the maximum sum of m sub-arrays would lie between max(nums) to sum(nums).
            Now we have to check which number between max(nums) and sum(nums) satisfies the split of nums into m pieces.
            This can be done using binary search.
        """
        minSum = max(nums)
        maxSum = sum(nums)
        if m == 1:
            return maxSum
        elif m >= len(nums):
            return minSum

        while minSum <= maxSum:
            midSum = minSum + ((maxSum - minSum) // 2)
            """
                Now how to check whether this midSum will satisfy the split of nums into m pieces and it would be the max sum among all the m sub-arrays.
                We will iterate the nums and keep adding the num of nums into sub array until its sum reaches the midSum. Once midSum is reached, we will take new sub array. Thus midSum would be the max sum among all m sub arrays.
            """
            subArrays = self.countSubArrays(nums, midSum)
            if subArrays > m:
                minSum = midSum + 1
            else:
                maxSum = midSum - 1

        return minSum

