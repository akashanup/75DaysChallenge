class Solution:
    def nextSmallerElement(self, nums):
        stack = [0]
        right = [-1] * len(nums)
        for index in range(1, len(nums)):
            while stack and nums[stack[-1]] > nums[index]:
                right[stack[-1]] = index
                stack.pop()
            stack.append(index)
        while stack:
            right[stack.pop()] = -1
        return right
    
    def previousSmallerElement(self, nums):
        stack = [len(nums)-1]
        left = [-1] * len(nums)
        for index in range(len(nums)-2, -1, -1):
            while stack and nums[stack[-1]] > nums[index]:
                left[stack[-1]] = index
                stack.pop()
            stack.append(index)
        while stack:
            left[stack.pop()] = -1
        return left
    
    def largestRectangleArea(self, heights: List[int]) -> int:
        right = self.nextSmallerElement(heights)
        left = self.previousSmallerElement(heights)
        area = 0
        for index, height in enumerate(heights):
            if right[index] == -1:
                right[index] = len(heights)
            area = max(area, height * (right[index] - left[index] - 1))
        return area