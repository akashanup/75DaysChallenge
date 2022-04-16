class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        lookup = {}
        stack = [nums2[0]]
        for num in nums2[1:]:
            while stack and num > stack[-1]:
                lookup[stack[-1]] = num
                stack.pop()
            stack.append(num)

        while stack:
            lookup[stack.pop()] = -1

        return [lookup[num] for num in nums1]
