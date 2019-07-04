class Solution:
    """
    @param matrix: a matrix of integers
    @param k: An integer
    @return: the kth smallest number in the matrix
    """
    def kthSmallest(self, matrix, k):
        if matrix is None or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        n = len(matrix)
        m = len(matrix[0])
        
        from queue import PriorityQueue
        pq = PriorityQueue()
        visited = set()
        
        pq.put((matrix[0][0], 0, 0))
        visited.add(0)
        
        for _ in range(k - 1):
            val, x, y = pq.get()
            _x = x + 1
            _y = y + 1
            _x_hash = _x * m + y
            _y_hash = x * m + _y
            
            if _x < n and _x_hash not in visited:
                pq.put((matrix[_x][y], _x, y))
                visited.add(_x_hash)
                
            if _y < m and _y_hash not in visited:
                pq.put((matrix[x][_y], x, _y))
                visited.add(_y_hash)
        
        return pq.get()[0]