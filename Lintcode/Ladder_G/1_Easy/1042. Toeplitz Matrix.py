class Solution:
    """
    @param matrix: the given matrix
    @return: True if and only if the matrix is Toeplitz
    """
    def isToeplitzMatrix(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        
        n = len(matrix)
        m = len(matrix[0])
        
        '''
        [[1,2,3,4],
         [5,1,2,3],
         [9,5,1,2]]
        '''
        
        # up to down
        for i in range(n):
            for step in range(1, n - i):
                if i + step >= m:
                    break
                
                if matrix[i][0] != matrix[i + step][step]:
                    return False
                    
        # left to right
        for j in range(1, m):
            for step in range(1, m - j):
                if j + step >= n:
                    break
                
                if matrix[0][j] != matrix[step][j + step]:
                    return False
        
        return True