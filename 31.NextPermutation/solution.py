class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
            Since we have to find the next greater permutation of array, we can think greedly by modifying only that part of array which will contribute in detemining the next greater permutation.
            Now, to determine the contributing sub-array, consider the below examples:
                - [1,2,3,4,5] -(next greater permutation)> [1,2,3,5,4]
                - [1,2,5,3,4] -(next greater permutation)> [1,2,5,4,3]
                - [1,2,4,3,5] -(next greater permutation)> [1,2,4,5,3]
                - [1,2,4,5,3] -(next greater permutation)> [1,2,5,4,3]->[1,2,5,3,4]
                - [1,3,5,4,2] -(next greater permutation)> [1,4,5,3,2]->[1,4,2,3,5]
                - [5,4,3,2,1] -(next greater permutation)> [1,2,3,4,5]
            From the above examples, we can see that if we traverse from end and check for the index(from right) from where the elements are not in descending order-
                - If found, it means that this index needs to be updated with the firs greater element from right to get any greater permutation and then to get the NEXT greater permutation we can reverse the array from further index to end as they were in decreasing order any by reversing, they will be in increasing order and that would be our next greater permutation.
                - Else, Complete array is in descending order so just make it into ascending by reversing it.
        """
        # Check for the index from right from where the array doesn't follows the descending order.
        i = len(nums)-2
        while i >= 0 and nums[i+1] <= nums[i]:
            i -= 1

        # If any such index is found then swap its value with the first greater element from right.
        if i >= 0:
            j = len(nums)-1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the further array items
        i += 1
        j = len(nums)-1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
