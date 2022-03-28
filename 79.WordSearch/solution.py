class Solution:
    def wordSearch(self, board, m, n, word, row, col, index):
        # word found!
        if index == len(word):
            return True
        # pointers became out of range of board
        if row < 0 or row >= m or col < 0 or col >= n:
            return False
        # char at index of word doesn't match with board's row,col
        if board[row][col] != word[index]:
            return False
        temp = board[row][col]
        # Set the current cell to None so that we can keep track of the visited cell.
        board[row][col] = None
        for x, y in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            if self.wordSearch(board, m, n, word, row + x, col + y, index + 1):
                return True
        # Backtrack
        board[row][col] = temp
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        # Check for word from each cell. If found then return True or at end return False
        for row in range(m):
            for col in range(n):
                if self.wordSearch(board, m, n, word, row, col, 0):
                    return True
        return False
