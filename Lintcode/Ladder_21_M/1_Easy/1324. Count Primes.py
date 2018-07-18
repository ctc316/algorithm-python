# Version 1: Naive with some optimization, Time: O(n * sqrt(n)), TLE
class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    def countPrimes(self, n):
        '''
            2, 3, 4, 5, 6, 7
            1  2  2  3  3  4
        '''
        import math

        primes = []
        for i in range(2, n):
            isPrime = True
            upper_bound = int(math.sqrt(i))
            for j in primes:
                if j > upper_bound:
                    break
                if i % j == 0:
                    isPrime = False
                    break

            if isPrime:
                primes.append(i)

        return len(primes)


# Version 2: 厄拉多塞筛法, Time: O(...)
'''
使用一個 boolean[]，紀錄數是否刪除;
然後遍歷，處理尚為 False 的數，取出来加入 primes
然後將其在 n 範圍內的倍數設置為 True 刪除
減少檢查已知的非質數工作
'''

class Solution:
    """
    @param n: a integer
    @return: return a integer
    """
    def countPrimes(self, n):
        '''
            2, 3, 4, 5, 6, 7
            1  2  2  3  3  4
        '''
        primes = []
        isDeleted = [False for i in range(0, n + 1)]
        for i in range(2, n):
            if isDeleted[i]:
                continue

            primes.append(i)
            for times in range(i, int(n / i) + 1):
                isDeleted[i * times] = True

        return len(primes)