class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix)-1, len(matrix[0])-1
        spiral = []

        r,c = 0, 0
        while r <= m and c <= n:
            if r <= m:
                spiral += matrix[r][c:n+1]
            r += 1

            if c <= n:
                spiral += [matrix[i][n] for i in range(r, m+1)]
            n -= 1

            if r <= m:
                spiral += matrix[m][c:n+1][::-1]
            m -= 1

            if c <= n:
                spiral += [matrix[i][c] for i in range(m, r-1, -1)]
            c += 1

        return spiral
