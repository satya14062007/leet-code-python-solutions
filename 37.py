class Solution:
    def solveSudoku(self, board):

        def isValid(row, col, num):
            # Check row
            for j in range(9):
                if board[row][j] == num:
                    return False

            # Check column
            for i in range(9):
                if board[i][col] == num:
                    return False

            # Check 3x3 box
            startRow = (row // 3) * 3
            startCol = (col // 3) * 3

            for i in range(startRow, startRow + 3):
                for j in range(startCol, startCol + 3):
                    if board[i][j] == num:
                        return False

            return True

        def solve():
            # Find an empty cell
            for i in range(9):
                for j in range(9):

                    if board[i][j] == '.':
                        
                        # Try numbers 1 to 9
                        for num in "123456789":

                            if isValid(i, j, num):
                                board[i][j] = num

                                # Recursively solve
                                if solve():
                                    return True

                                # Backtrack
                                board[i][j] = '.'

                        return False

            # No empty cells left
            return True

        solve()
