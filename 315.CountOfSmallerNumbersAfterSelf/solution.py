"""
Logic:
1. Since we want to know the number of elements in right that are smaller than current element, we could iterate from right to left and maintain a sorted list of every incoming number.
2. Whenever a new number come, we can do a binary search in that sorted list and find the leftmost correct index of current number then that index would be the number of smaller elements in right for any number.
3. For example,
	- nums => [5,2,6,2,5,2,1], sortedList = [], smaller = [-1,-1,-1,-1,-1,-1,-1]
	- Iterate from right to left:
		- When i is 6 then nums[6] is 1, its leftmost correct index in sortedList will be 0, therefore smaller[6] becomes 0. Now, sortedList = [1], smaller =  [-1,-1,-1,-1,-1,-1,0]
		- When i is 5 then nums[5] is 2, its leftmost correct index in sortedList will be 1, therefore smaller[5] becomes 1. Now, sortedList = [1,2], smaller =  [-1,-1,-1,-1,-1,1,0]
		- When i is 4 then nums[4] is 5, its leftmost correct index in sortedList will be 2, therefore smaller[4] becomes 2. Now, sortedList = [1,2,5], smaller =  [-1,-1,-1,-1,2,1,0]
		- When i is 3 then nums[3] is 2, its leftmost correct index in sortedList will be 1, therefore smaller[3] becomes 1. Now, sortedList = [1,2,2,5], smaller =  [-1,-1,-1,1,2,1,0]
		- When i is 2 then nums[2] is 6, its leftmost correct index in sortedList will be 4, therefore smaller[2] becomes 4. Now, sortedList = [1,2,2,5,6], smaller =  [-1,-1,4,1,2,1,0]
		- When i is 1 then nums[1] is 2, its leftmost correct index in sortedList will be 1, therefore smaller[1] becomes 1. Now, sortedList = [1,2,2,2,5,6], smaller =  [-1,1,4,1,2,1,0]
		- When i is 0 then nums[0] is 5, its leftmost correct index in sortedList will be 4, therefore smaller[0] becomes 4. Now, sortedList = [1,2,2,2,5,5,6], smaller =  [4,1,4,1,2,1,0]
"""

from sortedcontainers import SortedList


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        smaller = [-1] * n
        tempNums = SortedList()
        for key, num in enumerate(nums[::-1]):
            smaller[n - key - 1] = tempNums.bisect_left(num)
            tempNums.add(num)
        return smaller
