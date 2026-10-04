class Solution:
    def isValidSudoku(self, board):
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                num = board[i][j]

                # Find the 3x3 box number
                box = (i // 3) * 3 + (j // 3)

                # Check row
                if num in rows[i]:
                    return False

                # Check column
                if num in cols[j]:
                    return False

                # Check 3x3 box
                if num in boxes[box]:
                    return False

                # Add number
                rows[i].add(num)
                cols[j].add(num)
                boxes[box].add(num)

        return True
