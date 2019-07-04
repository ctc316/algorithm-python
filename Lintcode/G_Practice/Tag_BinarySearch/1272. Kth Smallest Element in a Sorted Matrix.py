class Solution:
    """
    @param matrix: List[List[int]]
    @param k: a integer
    @return: return a integer
    """
    def kthSmallest(self, matrix, k):
        '''
        [[ 1,  5,  9],
         [10, 11, 13],
         [12, 13, 15]]
        采用二分答案的方式来解决问题。
        我们知道答案一定在[minNum,maxNum]这个区间内。
        对于某一个数res，我们将其与矩阵中的每一个数作对比，
        统计比他大的数字的个数，如果个数正好等于k且res在矩阵中则答案为res。
        '''

        self.n = len(matrix)
        self.m = len(matrix[0])

        start = matrix[0][0]
        end = matrix[-1][-1]
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.get_num_less_equal(matrix, mid) < k:
                start = mid
            else:
                end = mid

        if self.get_num_less_equal(matrix, start) >= k:
            return start
        return end


    def get_num_less_equal(self, matrix, mid):
        i = 0
        j = self.m - 1
        count = 0
        while i < self.n and j >= 0:
            if matrix[i][j] <= mid:
                i += 1
                count += j + 1
            else:
                j -= 1
        return count