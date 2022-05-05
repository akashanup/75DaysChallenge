import time


class Solution:

    KNIGHT_MOVES = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]

    def recur(self, mat, n, r, c, moves):
        if moves == n*n:
            return True

        for dr, dc in Solution.KNIGHT_MOVES:
            if 0 <= r+dr < n and 0 <= c+dc < n and mat[r+dr][c+dc] == -1:
                mat[r+dr][c+dc] = moves
                if self.recur(mat, n, r+dr, c+dc, moves+1):
                    return True
                mat[r+dr][c+dc] = -1

        return False

    def knightTour(self, n):
        mat = [[-1 for _ in range(n)] for _ in range(n)]
        mat[0][0] = 0
        self.recur(mat, n, 0, 0, 1)
        return mat
