class Solution:
    """
    @param n: an integer
    @return: return the matrix
    """
    def magicSquare(self, n):
        result, _ = self.build_sems(n) if n % 2 == 0 else self.build_oms(n)
        return result
    
    def build_oms(self, s):
        if s % 2 == 0:
            s += 1
        q = [[0 for j in range(s)] for i in range(s)]
        p = 1
        i = s // 2
        j = 0
        while p <= (s * s):
            q[i][j] = p
            ti = i + 1
            if ti >= s: ti = 0
            tj = j - 1
            if tj < 0: tj = s - 1
            if q[ti][tj] != 0:
                ti = i
                tj = j + 1
            i = ti
            j = tj
            p = p + 1
     
        return q, s
 
 
    # build singly even magic square
    def build_sems(self, s):
        if s % 2 == 1:
            s += 1
        while s % 4 == 0:
            s += 2
     
        q = [[0 for j in range(s)] for i in range(s)]
        z = s // 2
        b = z * z
        c = 2 * b
        d = 3 * b
        o = self.build_oms(z)
     
        for j in range(0, z):
            for i in range(0, z):
                a = o[0][i][j]
                q[i][j] = a
                q[i + z][j + z] = a + b
                q[i + z][j] = a + c
                q[i][j + z] = a + d
     
        lc = z // 2
        rc = lc
        for j in range(0, z):
            for i in range(0, s):
                if i < lc or i > s - rc or (i == lc and j == lc):
                    if not (i == 0 and j == lc):
                        t = q[i][j]
                        q[i][j] = q[i][j + z]
                        q[i][j + z] = t
     
        return q, s
     
     



     
class Solution:
    """
    @param n: an integer
    @return: return the matrix
    """
    def magicSquare(self, n):
        '''
        [[4,9,2],
         [3,5,7],
         [8,1,6]]

         n = 3
         sum = 9(10) / 2 = 45
         row avg = 45 / 3 = 15

         sum = n^2(n^2+1)/2
         row avg = sum/n
        '''

        self.n = n
        self.maxi = n * n
        self.avg = int(n * n * (n * n + 1) / 2 / n)
        result = self.dfs([i + 1 for i in range(n * n)], [[0 for _ in range(n)] for __ in range(n)], 0)
        print(result)
        return result


    def dfs(self, options, matrix, pos):
        if len(options) == 0:
            return matrix if self.checkDiagonal(matrix) else None

        row = int(pos / self.n)
        col = pos % self.n
        for i in range(len(options)):
            matrix[row][col] = options[i]
            if self.check(matrix, row, col, min(options)):
                temp = options.pop(i)
                result = self.dfs(options, matrix, pos + 1)
                if result is not None:
                    return result
                options.insert(i, temp)
            matrix[row][col] = 0

        return None

    def check(self, matrix, row, col, minimum):
        # row
        summ = 0
        zeros = 0
        for i in range(self.n):
            if matrix[row][i] == 0:
                zeros += 1
            summ += matrix[row][i]

        # print("row:", summ, zeros)
        if zeros == 0:
            if summ != self.avg:
                return False
        elif summ + minimum > self.avg:
                return False


        # cols
        summ = 0
        zeros = 0
        for i in range(self.n):
            if matrix[i][col] == 0:
                zeros += 1
            summ += matrix[i][col]

        # print("col:", summ, zeros)
        if zeros == 0:
            if summ != self.avg:
                return False
        elif summ + minimum > self.avg:
                return False

        return True


    def checkDiagonal(self, matrix):
        summ1 = 0
        summ2 = 0
        for i in range(self.n):
            summ1 += matrix[i][i]
            summ2 += matrix[self.n - 1 - i][i]

        return summ1 == self.avg and summ2 == self.avg