class Solution:
    def applyChanges(self, grid, m, n, r, c):
        live = 0
        if c > 0:
            if grid[r][c - 1] in (1, 2):
                live += 1
        if c < n - 1:
            if grid[r][c + 1] in (1, 2):
                live += 1

        if r > 0:
            if grid[r - 1][c] in (1, 2):
                live += 1
            if c > 0:
                if grid[r - 1][c - 1] in (1, 2):
                    live += 1
            if c < n - 1:
                if grid[r - 1][c + 1] in (1, 2):
                    live += 1

        if r < m - 1:
            if grid[r + 1][c] in (1, 2):
                live += 1
            if c > 0:
                if grid[r + 1][c - 1] in (1, 2):
                    live += 1
            if c < n - 1:
                if grid[r + 1][c + 1] in (1, 2):
                    live += 1

        # 2: Became dead from alive
        # 3: Became alive from dead
        if grid[r][c] == 1:
            if live < 2 or live > 3:
                return 2
        else:
            if live == 3:
                return 3
        return grid[r][c]

    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        for r in range(m):
            for c in range(n):
                board[r][c] = self.applyChanges(board, m, n, r, c)
        print(board)
        for r in range(m):
            for c in range(n):
                if board[r][c] == 2:
                    board[r][c] = 0
                elif board[r][c] == 3:
                    board[r][c] = 1
