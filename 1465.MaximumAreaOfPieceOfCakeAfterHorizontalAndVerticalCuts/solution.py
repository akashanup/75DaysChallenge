class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        verticalCuts.sort()

        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]

        """
            Since we are cutting the pieces in horizontally and vertically.
            Therefore, the maximum height of any piece would be the maximum difference between two consecutive cuts in horizontalCuts and the maximum width of any piece would be the maximum difference between two consecutive cuts in verticalCuts.
            Therefore, the maximum area of a piece would be of a piece having maximum height and maximum width.
        """

        maxWidth = 0
        for x in range(1, len(verticalCuts)):
            maxWidth = max(maxWidth, verticalCuts[x]-verticalCuts[x-1])

        maxHeight = 0
        for y in range(1, len(horizontalCuts)):
            maxHeight = max(maxHeight, horizontalCuts[y]-horizontalCuts[y-1])

        return (maxWidth * maxHeight) % ((10**9)+7)
