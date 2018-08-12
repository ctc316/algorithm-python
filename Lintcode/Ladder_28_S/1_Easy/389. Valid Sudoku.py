class Solution:
    """
    @param board: the board
    @return: whether the Sudoku is valid
    """
    def isValidSudoku(self, board):
        n = len(board)
        for row in range(n):
            hash = set()
            for col in range(n):
                if board[row][col] == ".":
                    continue
                if board[row][col] in hash:
                    return False
                hash.add(board[row][col])

        for col in range(n):
            hash = set()
            for row in range(n):
                if board[row][col] == ".":
                    continue
                if board[row][col] in hash:
                    return False
                hash.add(board[row][col])

        for left in range(0, n, 3):
            for top in range(0, n, 3):
                hash = set()
                for row in range(left, left + 3):
                    for col in range(top, top + 3):
                        if board[row][col] == ".":
                            continue
                        if board[row][col] in hash:
                            return False
                        hash.add(board[row][col])

        return True