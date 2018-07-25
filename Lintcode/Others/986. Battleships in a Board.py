class Solution:
    """
    @param board: the given 2D board
    @return: the number of battle ships
    """
    def countBattleships(self, board):
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != "X" or \
                   i - 1 >= 0 and board[i - 1][j] == "X" or  \
                   j - 1 >= 0 and board[i][j - 1] == "X":
                    continue

                count += 1

        return count