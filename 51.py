class Solution:
    def solveNQueens(self, n: int):
        result = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row):
            if row == n:
                solution = []
                for r in board:
                    solution.append("".join(r))
                result.append(solution)
                return

            for col in range(n):
                if is_safe(row, col):
                    board[row][col] = "Q"
                    backtrack(row + 1)
                    board[row][col] = "."

        def is_safe(row, col):
            # Check column
            for r in range(row):
                if board[r][col] == "Q":
                    return False

            # Check upper-left diagonal
            r, c = row - 1, col - 1
            while r >= 0 and c >= 0:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c -= 1

            # Check upper-right diagonal
            r, c = row - 1, col + 1
            while r >= 0 and c < n:
                if board[r][c] == "Q":
                    return False
                r -= 1
                c += 1

            return True

        backtrack(0)
        return result
