class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        maxArea = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    queue = [(row, col)]
                    grid[row][col] = 0
                    tempArea = 0
                    while queue:
                        r, c = queue.pop(0)
                        tempArea += 1
                        for dr, dc in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                            if 0 <= dr < m and 0 <= dc < n and grid[dr][dc] == 1:
                                grid[dr][dc] = 0
                                queue.append((dr, dc))
                    maxArea = max(maxArea, tempArea)
        return maxArea
