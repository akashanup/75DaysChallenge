class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        lookup = [-1] * n
        stack = [0]
        i = 1
        """
            It is similar to Next Greater Element I (https://leetcode.com/problems/next-greater-element-i/discuss/1529683/Python-or-Simple-Solutions)
            The only difference over here is that the array is now circular. 
            So the max length to search for an element at index j would be from j+1 to n and then from 0 to j-1. This search space can be easily encountered using modulo(%) operator as it will again result the index from 0 after it reaches the length of array.
            One more thing that needs to be taken care of is, here we will not add the element directly to stack. First we will check whether its next greater elemnt has been found or not. If not found then add it to stack.
        """
        while i < 2*n:
            while stack and nums[i%n] > nums[stack[-1]]:
                lookup[stack[-1]] = nums[i%n]
                stack.pop()
            if lookup[i%n] == -1:
                stack.append(i%n)
            i += 1
        return lookup            
