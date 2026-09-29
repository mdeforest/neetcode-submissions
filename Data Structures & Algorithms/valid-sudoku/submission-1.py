import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[False] * 9 for _ in range(9)]
        cols = [[False] * 9 for _ in range(9)]
        squares = [[False] * 9 for _ in range(9)]

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                
                if value == '.':
                    continue

                value = int(value)

                # rows
                if rows[r][value - 1]:
                    return False
                else:
                    rows[r][value - 1] = True

                # cols
                if cols[c][value - 1]:
                    print("cols")
                    return False
                else:
                    cols[c][value - 1] = True

                # square
                square = 3 * math.floor(r / 3) + math.floor(c / 3)

                if squares[square][value - 1]:
                    return False
                else:
                    squares[square][value - 1] = True


        return True
