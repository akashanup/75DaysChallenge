class Solution:
    def recur(self, mat, r, c, path):
        if r == len(mat) or c == len(mat[0]) or mat[r][c] == 0:
            return False
        path.append((r, c))
        if r == len(mat)-1 and c == len(mat[0])-1:
            return True
        mat[r][c] = 0
        if self.recur(mat, r+1, c, path) or self.recur(mat, r, c+1, path):
            return True
        # Backtrack
        mat[r][c] = 1
        path.pop()

    def findPath(self, mat):
        pathMatrix = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        path = []
        self.recur(mat, 0, 0, path)
        for r, c in path:
            pathMatrix[r][c] = 1
        return pathMatrix


print(Solution().findPath([[1, 0, 0, 0], [1, 1, 0, 1], [0, 1, 0, 0], [1, 1, 1, 1]]))
