class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        partitionIndex = None
        for i in range(len(nums)):
            if nums[i] > 0:
                partitionIndex = i
                break

        # Squaring each element
        for i in range(len(nums)):
            nums[i] *= nums[i]

        # If all the elements were > 0 initially: Return their squares
        if partitionIndex == 0:
            return nums

        # If all the elements were <= 0 initially: Return their squares in reverse
        if partitionIndex is None:
            return nums[::-1]

        # If elements were combination of positive and negative numbers:
        # Divide the initial array into positive and negative arrays based on partitionIndex
        # Merge both the arrays in non-decreasing order.
        i, x, y = 0, partitionIndex - 1, partitionIndex
        squareSortedArray = [None] * len(nums)
        while x >= 0 and y < len(nums):
            if nums[x] <= nums[y]:
                squareSortedArray[i] = nums[x]
                x -= 1
            else:
                squareSortedArray[i] = nums[y]
                y += 1
            i += 1

        while x >= 0:
            squareSortedArray[i] = nums[x]
            x -= 1
            i += 1

        while y < len(nums):
            squareSortedArray[i] = nums[y]
            y += 1
            i += 1

        return squareSortedArray
