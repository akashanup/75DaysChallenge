"""
Logic:
    Initially calculate the area with maximum possible width (start, end) i.e, (0, len(height)-1).
    Keep on decreasing the width assuming that there would be a higher line in between the above width as follows-
        1. If height of starting line is greater than the end then calculate for (start+1, end)
        2. Else calculate for (start, end-1)
    Now the question boils down to simple 2 pointer problem.
"""


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        start = 0
        end = len(height)-1
        while start < end:
            maxArea = max(maxArea, min(height[start], height[end])*(end-start))
            if height[start] > height[end]:
                end -= 1
            else:
                start += 1
        return maxArea
