class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """
    def spiralOrder(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        n = len(matrix)
        m = len(matrix[0])
        visited = [[False for _ in range(m)] for _ in range(n)]
        res = []
        x, y = 0, 0
        ORDERED_MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        n_moves = len(ORDERED_MOVES)
        moveIdx = 0
        hasNext = True
        while hasNext:
            res.append(matrix[x][y])
            visited[x][y] = True
            hasNext = False
            for i in range(n_moves):
                mi = (moveIdx + i) % n_moves
                x_ = x + ORDERED_MOVES[mi][0]
                y_ = y + ORDERED_MOVES[mi][1]
                if x_ >= 0 and x_ < n and y_ >= 0 and y_ < m and not visited[x_][y_]:
                    x, y = x_, y_
                    moveIdx = mi
                    hasNext = True
                    break

        return res