class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):
        '''
        scan from bottom-left corner to top-right corner
        [[1,3,5,7],    3
         [3,11,16,20],
         [23,30,34,50]]
        '''
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        n = len(matrix)
        m = len(matrix[0])
        row = n - 1
        col = 0
        count = 0

        while row >= 0 and col < m:
            if matrix[row][col] < target:
                col += 1
            else:
                if matrix[row][col] == target:
                    count += 1
                row -= 1
        return count