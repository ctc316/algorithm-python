class Solution:
    """
    @param matrix: a matrix of m x n elements
    @return: an integer list
    """
    def spiralOrder(self, matrix):
        '''
        [[1,2,3,4],
         [6,7,8,9],
         [10,11,12,13],
         [20,21,22,23]]
        [1,2,3,4,9,13,23,22,21,20,10,11,12,8,7,6]
        '''
        n = len(matrix)
        if n == 0:
            return []
            
        m = len(matrix[0])
        if m == 0:
            return []
            
        MOVES = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        total = n * m
        visited = set()
        x, y = 0, 0
        results = [matrix[0][0]]
        visited.add(0)
        last_move = 0
        
        while len(visited) < total:
            for i in range(4):
                move_idx = (last_move + i) % 4
                x_ = x + MOVES[move_idx][0]
                y_ = y + MOVES[move_idx][1]
                if x_ < 0 or x_ >= n or y_ < 0 or y_ >= m:
                    continue
                
                if x_ * m + y_ in visited:
                    continue
                
                visited.add(x_ * m + y_)
                results.append(matrix[x_][y_])
                x, y = x_, y_
                last_move = move_idx
                break
        
        return results
                