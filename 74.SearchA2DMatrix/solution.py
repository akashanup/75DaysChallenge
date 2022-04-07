class Solution:
    def binarySearchInRow(self, matrix, row, colStart, colEnd, target):
        while colStart <= colEnd:
            midCol = colStart + ((colEnd - colStart) // 2)
            if matrix[row][midCol] == target:
                return True
            elif matrix[row][midCol] > target:
                colEnd = midCol - 1
            else:
                colStart = midCol + 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        lastCol = len(matrix[0]) - 1
        startRow = 0
        endRow = len(matrix) - 1
        # If we have only one row then simple binary search in that row
        if endRow == 0:
            return self.binarySearchInRow(matrix, 0, 0, lastCol, target)
        midCol = lastCol // 2
        """
            Since we have to write an efficient algorithm to search a target in matrix, we will be reducing our search space by utilising the following  facts-
                1. Integers in each row are sorted from left to right.
                2. The first integer of each row is greater than the last integer of the previous row.

            Let us try to search from middle column(or row) and try to reduce the search space.
            Now suppose,
                1. If target is less then matrix[startRow][midCol] then target will definitely be present either on that row or previous rows.
                2. If target is greater then matrix[startRow][midCol] then target will definitely be present either on that row or next rows.
            So we can eliminate the unnecessary rows and search only in potential rows which may have target.
            
            At the end we might be left with two rows which may have target. We can classify these rows into four parts and apply binary search.
                1. Part1 would be the first row from start column till middle column
                2. Part2 would be the first row from middle column till last column
                3. Part3 would be the second row from start column till middle column
                4. Part4 would be the second row from middle column till last column
        """
        while startRow < endRow - 1:
            midRow = startRow + ((endRow - startRow) // 2)
            if matrix[midRow][midCol] == target:
                return True
            elif matrix[midRow][midCol] > target:
                endRow = midRow
            else:
                startRow = midRow

        # If target is not found yet then we are left with two rows to search for target as expained above.
        # Search in Part1 if applicable
        if target <= matrix[startRow][midCol]:
            return self.binarySearchInRow(matrix, startRow, 0, midCol, target)
        if matrix[startRow][midCol] < target <= matrix[startRow][lastCol]:
            return self.binarySearchInRow(matrix, startRow, midCol + 1, lastCol, target)
        if target <= matrix[startRow+1][midCol]:
            return self.binarySearchInRow(matrix, startRow + 1, 0, midCol, target)
        else:
            return self.binarySearchInRow(matrix, startRow+1, midCol + 1, lastCol, target)
