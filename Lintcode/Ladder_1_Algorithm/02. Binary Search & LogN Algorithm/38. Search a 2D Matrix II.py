class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def searchMatrix(self, matrix, target):

        """
        [1, 3, 5, 7],
        [2, 4, 7, 8],
        [3, 5, 9, 10]

        start from left bottom,
        """

        if matrix == [] or matrix[0] == []:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        row, col = n - 1, 0
        count = 0
        while row >= 0 and col < m:
            if target < matrix[row][col]:
                row -= 1
            elif target > matrix[row][col]:
                col += 1
            else:
                row -= 1
                col += 1
                count += 1

        return count