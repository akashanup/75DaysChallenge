class Solution:
    def dfs(self, grid, r, c):
        if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
            return 0
        if grid[r][c] == 1:
            grid[r][c] = 0
            return 1 + self.dfs(grid, r+1, c) + self.dfs(grid, r-1, c) + self.dfs(grid, r, c-1) + self.dfs(grid, r, c+1)
        return 0

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxArea = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    maxArea = max(maxArea, self.dfs(grid, row, col))
        return maxArea
