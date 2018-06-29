class Solution:
    """
    @param: matrix: an integer matrix
    @return: the coordinate of the left-up and right-down number
    """
    def submatrixSum(self, matrix):

        '''
         [[1,5,7],
          [3,7,-8],
          [4,-8,9]]

         [[0, 0, 0, 0],
          [0, 1, 6, 13],
          [0, 4, 16, 15],
          [0, 8, 12, 20]
        '''
        n = len(matrix)
        m = len(matrix[0])
        dp = [[0 for _ in range(m + 1)] for __ in range(n + 1)]
        for r in range(n):
            for d in range(m):
                # r, d  -> right-down
                # fill the table,
                dp[r + 1][d + 1] = matrix[r][d] + dp[r + 1][d] + dp[r][d + 1] - dp[r][d]

                # check combinations before
                for l in range(r + 1):
                    for u in range(d + 1):
                        if dp[r + 1][d + 1] - dp[l][d + 1] - dp[r + 1][u] + dp[l][u] == 0:
                            return [(l, u), (r, d)]