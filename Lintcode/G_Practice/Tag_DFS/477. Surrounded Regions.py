class Solution:
    """
    @param: board: board a 2D board containing 'X' and 'O'
    @return: nothing
    """
    def surroundedRegions(self, board):
        if not board or len(board) == 0 or len(board[0]) == 0:
            return

        n = len(board)
        m = len(board[0])
        reached = [[False for _ in range(m)] for _ in range(n)]

        for i in range(n):
            if board[i][0] == 'O' and not reached[i][0]:
                self.dfs(board, n, m, i, 0, reached)
            if board[i][-1] == 'O' and not reached[i][-1]:
                self.dfs(board, n, m, i, m - 1, reached)

        for j in range(1, m - 1):
            if board[0][j] == 'O' and not reached[0][j]:
                self.dfs(board, n, m, 0, j, reached)
            if board[-1][j] == 'O' and not reached[-1][j]:
                self.dfs(board, n, m, n - 1, j, reached)

        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if board[i][j] == 'O' and not reached[i][j]:
                    board[i][j] = 'X'


    def dfs(self, board, n, m, i, j, reached):
        reached[i][j] = True
        for adj in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            x = i + adj[0]
            y = j + adj[1]
            if x < 0 or x >= n or y < 0 or y >= m or reached[x][y] or board[x][y] != 'O':
                continue
            self.dfs(board, n, m, x, y, reached)
