'''
Given a non-empty 2D matrix matrix and an integer k,
find the max sum of a rectangle in the matrix such that its sum is no larger than k.

1.The rectangle inside the matrix must have an area > 0.
2.What if the number of rows is much larger than the number of columns?

Example
Given matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2


The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is the max number no larger than k (k = 2).
'''




class Solution:
    """
    @param matrix: a 2D matrix
    @param k: an integer
    @return: the max sum of a rectangle in the matrix such that its sum is no larger than k
    """
    def maxSumSubmatrix(self, matrix, k):
        '''
        [[5,-4,-3,4],
         [-3,-4,4,5],
          [5,1,5,-4]]

         [[0, 0, 0, 0, 0],
          [0, 5, 1, -2, 2],
          [0, 2, -6, -5, 4],
          [0, 7, 0, 6, 11]]
        '''
        if not matrix or len(matrix) == 0 or len(matrix[0]) == 0:
            return 0

        n = len(matrix)
        m = len(matrix[0])

        prefixSum = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        max_sum = -float("Inf")
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prefixSum[i][j] = matrix[i - 1][j - 1] + prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1]

                if prefixSum[i][j] == k:
                    return k

                for p in range(1, i + 1):
                    for q in range(1, j + 1):
                        area = prefixSum[i][j] - prefixSum[p - 1][j] - prefixSum[i][q - 1] + prefixSum[p - 1][q - 1]
                        if area > k:
                            continue
                        max_sum = max(max_sum, area)

                if max_sum == k:
                    return k

        return max_sum