"""
Logic:
    Initially calculate the area with maximum possible width (start, end) i.e, (0, len(height)-1).
    Keep on decreasing the width assuming that there would be a higher line in between the above width as follows-
        1. If height of starting line is greater than the end then calculate for (start+1, end)
        2. Else calculate for (start, end-1)
    Now the question boils down to simple 2 pointer problem.
"""


class Solution:
    def recur(self, height, start, end, area):
        if start < end:
            maxArea = max(area, min(height[start], height[end])*(end-start))
            if height[start] > height[end]:
                maxArea = max(maxArea, self.recur(height, start, end-1, area))
            else:
                maxArea = max(maxArea, self.recur(height, start+1, end, area))
            return maxArea
        return 0

    def maxArea(self, height: List[int]) -> int:
        return self.recur(height, 0, len(height)-1, 0)
