class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        """
            Since the grid is sorted in non increasing order among rows and columns.
            So let's start searching from last row and first column for the negative value because numbers after that column and below that row will definitely be -ve.        
        """

        row, col = m-1, 0
        negatives = 0

        while row >= 0 and col < n:
            if grid[row][col] < 0:
                negatives += (n - col)
                row -= 1
            else:
                col += 1
        return negatives
