# Version 1: Fast Matrix Exponential  o((logm) * n)
class Matrix:
    def __init__(self, rows=0, cols=0, isUnit=False, copyFrom=None):
        if isinstance(copyFrom, Matrix):
            self.rows = copyFrom.rows
            self.cols = copyFrom.cols
            self.matrix = [[v for v in row] for row in copyFrom.matrix]
            return

        self.rows = rows
        self.cols = cols
        self.matrix = [[0 for _ in range(cols)] for __ in range(rows)]

        if isUnit:
            for i in range(min(self.rows, self.cols)):
                self.matrix[i][i] = 1


    def multiply(self, target):
        resultMat = Matrix(self.rows, target.cols)
        for i in range(self.rows):
            for j in range(target.cols):
                for k in range(self.cols):
                    resultMat.matrix[i][j] += self.matrix[i][k] * target.matrix[k][j]
                    resultMat.matrix[i][j] %= 10000007

        return resultMat


    '''
        Odd:   res = res * multi
        Even:  multi = multi * multi
        example:
             6 -> 3 -> 2 -> 1
            m=2  m=2  m=4  m=4
            r=0  r=2  r=2  r=6
    '''
    def power(self, n):
        resultMat = Matrix(self.rows, self.cols, True)
        multiMat = Matrix(copyFrom=self)
        while n > 0:
            if n % 2 == 1:
                resultMat = resultMat.multiply(multiMat)
                n -= 1
            else:
                multiMat = multiMat.multiply(multiMat)
                n = int(n / 2)

        return resultMat


class Solution:
    """
    @param X: a list of integers
    @param m: an integer
    @return: return an integer
    """
    def calcTheValueOfAnm(self, X, m):
        '''
        [0, 233, 2333,  23333 ]
        [1,"234" 2567,  25900 ]
        [2, 236 "2803", 28703 ]
        [3, 239  3042, "28942"]
        [4, 243  3285         ]
        [5, 248               ]

        [3, 23, 1, 2, 3, 4, 5]      [1] [1] [1] [1] [1] [1] [1]
                                    [0][10][10][10][10][10][10]
                                    [0] [0] [1] [1] [1] [1] [1]
                                    [0] [0] [0] [1] [1] [1] [1]
                                    [0] [0] [0] [0] [1] [1] [1]
                                    [0] [0] [0] [0] [0] [1] [1]
                                    [0] [0] [0] [0] [0] [0] [1]

        '''

        n = len(X)
        if n < 1 and m < 1:
            return 0

        # initialize base matrix
        baseMat = Matrix(1, n + 2)
        baseMat.matrix[0][0] = 3
        baseMat.matrix[0][1] = 23
        for i in range(n):
            baseMat.matrix[0][i + 2] = X[i] % 10000007

        # initialize transfer matrix
        transMat = Matrix(n + 2, n + 2)
        for i in range(n + 2):
            transMat.matrix[0][i] = 1
        for i in range(1, n + 2):
            transMat.matrix[1][i] = 10
        for i in range(2, n + 2):
            for j in range(i, n + 2):
                transMat.matrix[i][j] = 1

        return baseMat.multiply(transMat.power(m)).matrix[0][-1]





# Version 2: DP, Time: O(n * m), TLE 
class Solution:
    """
    @param X: a list of integers
    @param m: an integer
    @return: return an integer
    """
    def calcTheValueOfAnm(self, X, m):
        '''
        [0,     233, 2333, 23333, ...]
        [X[0],
        [X[1],

        '''

        n = len(X)
        if n < 1 and m < 1:
            return 0
        if m < 1:
            return X[-1]
        if n < 1:
            num = 23
            result = 0
            for _ in range(m):
                num = (num * 10 + 3) % 10000007
            return num


        num = 23
        for j in range(m):
            num = (num * 10 + 3) % 10000007
            for i in range(n):
                if i == 0:
                    X[i] += num
                else:
                    X[i] += X[i - 1]

                X[i] %= 10000007

        return X[n - 1]