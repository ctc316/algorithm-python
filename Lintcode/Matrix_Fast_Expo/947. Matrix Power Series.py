# Version 1:  Matrix Fast Exponential, Time: O(logk * (row * col)),   TLE
class Matrix:
    def __init__(self, rows=0, cols=0, isUnit=False, copyFrom=None, mod=1):
        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for _ in range(cols)] for __ in range(rows)]
        self.mod = mod

        if isUnit:
            for i in range(min(rows, cols)):
                self.matrix[i][i] = 1


    def multiply(self, target):
        result = Matrix(self.rows, target.cols, mod=self.mod)
        for i in range(self.rows):
            for j in range(target.cols):
                for k in range(self.cols):
                    result.matrix[i][j] += self.matrix[i][k] * target.matrix[k][j]
                    result.matrix[i][j] %= self.mod

        return result


    def plus(self, target):
        result = Matrix(self.rows, self.cols, mod=self.mod)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] = self.matrix[i][j] + target.matrix[i][j]
                result.matrix[i][j] %= self.mod

        return result


class Solution:
    """
    @param A: a n x n matrix
    @param k: a integer
    @param m: a integer
    @return: return a 2D arrays, denote S matrix
    """
    def matrixPowerSeries(self, A, k, m):
        '''
        S1 = 0  + A1
        S2 = S1 + A2
        S3 = S2 + A3

         A    S
        [A1   0]        [A][1]
                        [0][1]

        [A2   A1]
        [A3   A1 + A2]
        [A4   A1 + A2 + A3]

        '''

        rows = len(A)
        if rows == 0:
            return []
        cols = len(A[0])
        if cols == 0:
            return []

        # 0 and 1 matrix
        Zero = Matrix(rows, cols, mod=m)
        One = Matrix(rows, cols, isUnit=True, mod=m)

        # A matrix
        A_mat = Matrix(rows, cols, mod=m)
        for i in range(rows):
            for j in range(cols):
                A_mat.matrix[i][j] = A[i][j] % m

        # transfer matrix
        trans_mat = [[One, Zero], [Zero, One]]
        multi_mat = [[A_mat, One], [Zero, One]]

        # exponential
        while k > 0:
            if k % 2 == 1:
                trans_mat = self.dotMatrixInMatrix(trans_mat, multi_mat, Zero, One)
                k -= 1
            else:
                multi_mat = self.dotMatrixInMatrix(multi_mat, multi_mat, Zero, One)
                k = int(k / 2)

        result_mat = self.dotMatrixInMatrix([[A_mat, Zero]], trans_mat, Zero, One)
        return result_mat[0][-1].matrix


    def dotMatrixInMatrix(self, A, B, Zero, One):
        n = len(A)
        m = len(B[0])
        result = [[Zero for _ in range(m)] for __ in range(n)]
        for i in range(n):
            for j in range(m):
                for k in range(len(A[0])):
                    if A[i][k] is Zero or B[k][j] is Zero:
                        continue

                    if A[i][k] is One:
                        result[i][j] = result[i][j].plus(B[k][j])
                    elif B[k][j] is One:
                        result[i][j] = result[i][j].plus(A[i][k])
                    else:
                        result[i][j] = result[i][j].plus(A[i][k].multiply(B[k][j]))

        return result




# Version 2: simple add, Time: O(N), TLE
class Matrix:
    def __init__(self, rows=0, cols=0, isUnit=False, copyFrom=None, mod=1):
        if isinstance(copyFrom, Matrix):
            self.rows = copyFrom.rows
            self.cols = copyFrom.cols
            self.matrix = [[v for v in row] for row in copyFrom]
            self.mod = copyFrom.mod
            return

        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for _ in range(cols)] for __ in range(rows)]
        self.mod = mod

        if isUnit:
            for i in range(min(rows, cols)):
                self.matrix[i][i] = 1


    def multiply(self, target):
        result = Matrix(self.rows, target.cols, mod=self.mod)
        for i in range(self.rows):
            for j in range(target.cols):
                for k in range(self.cols):
                    result.matrix[i][j] += self.matrix[i][k] * target.matrix[k][j]
                    result.matrix[i][j] %= self.mod

        return result


    def plus(self, target):
        result = Matrix(self.rows, self.cols, mod=self.mod)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] = self.matrix[i][j] + target.matrix[i][j]
                result.matrix[i][j] %= self.mod

        return result


class Solution:
    """
    @param A: a n x n matrix
    @param k: a integer
    @param m: a integer
    @return: return a 2D arrays, denote S matrix
    """
    def matrixPowerSeries(self, A, k, m):
        '''
        (1)         S = A + A^2 + ... + A^k
        (2)     S * A =     A^2 + ... + A^k + A^k+1
        (2)-(1)   (A - 1)S = (A^k+1 - A)
                         S = (A - 1)^-1 * (A^k+1 - A)
        '''

        rows = len(A)
        if rows == 0:
            return 0

        cols = len(A[0])
        if cols == 0:
            return 0

        # init A matrix
        A_mat = Matrix(rows, cols, mod=m)
        for i in range(rows):
            for j in range(cols):
                A_mat.matrix[i][j] = A[i][j]

        result = Matrix(rows, cols, mod=m)
        cumu_mat = Matrix(rows, cols, isUnit=True, mod=m)

        for _ in range(k):
            cumu_mat = cumu_mat.multiply(A_mat)
            result = result.plus(cumu_mat)

        return result.matrix