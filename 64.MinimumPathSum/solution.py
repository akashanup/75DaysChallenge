import sys


class Solution:
    def dp(self, grid, r, c, lookup):
        if r == len(grid) - 1 and c == len(grid[0]) - 1:
            return grid[-1][-1]
        if r == len(grid) or c == len(grid[0]):
            return sys.maxsize
        if (r, c) not in lookup:
            lookup[(r, c)] = grid[r][c] + min(self.dp(grid, r + 1, c, lookup), self.dp(grid, r, c + 1, lookup))
        return lookup[(r, c)]

    def minPathSum(self, grid: List[List[int]]) -> int:
        return self.dp(grid, 0, 0, {})
