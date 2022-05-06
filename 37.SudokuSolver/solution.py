class Solution:
    def getEmptyCell(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':
                    # Empty cell found!
                    return row, col
        # No empty cell left
        return None, None

    def isValid(self, board, row, col, num):
        # Check in that row
        if num in board[row]:
            return False
        # Get that column
        boardColumn = [board[i][col] for i in range(9)]
        if num in boardColumn:
            return False
        # Check in that block
        blockRowStartIndex = (row // 3) * 3
        blockColStartIndex = (col // 3) * 3
        for r in range(blockRowStartIndex, blockRowStartIndex+3):
            for c in range(blockColStartIndex, blockColStartIndex+3):
                if board[r][c] == num:
                    return False
        return True

    def applyGuesses(self, board):
        row, col = self.getEmptyCell(board)
        if row is None:
            return True
        for guess in range(1, 10):
            if self.isValid(board, row, col, str(guess)):
                board[row][col] = str(guess)
                if self.applyGuesses(board) is True:
                    return True
            board[row][col] = '.'
        return False

    def solveSudoku(self, board: List[List[str]]) -> None:
        if self.applyGuesses(board) is True:
            return board
        return -1
