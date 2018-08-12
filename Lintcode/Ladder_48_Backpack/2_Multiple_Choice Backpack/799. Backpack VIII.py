# Version 1: TLE
class Solution:
    """
    @param n: the value from 1 - n
    @param value: the value of coins
    @param amount: the number of coins
    @return: how many different value
    """
    def backPackVIII(self, n, value, amount):
        '''
            5
            [1,2,4]
            [2,1,1]

            [1,0,0,0,0,0]
            [1,1,0,0,0,0]
            [1,1,1,0,0,0]
            [1,1,1,1,1,0]
            [1,1,1,1,1,1]

        '''
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        for i in range(len(value)):
            for j in range(amount[i]):
                for k in range(n, value[i] - 1, -1):
                    dp[k] = dp[k] or dp[k - value[i]]

        count = 0
        for i in range(1, n + 1):
            if dp[i]:
                count += 1

        return count


# Version 2: 兩層循環，每個硬幣循環，加入used[]計算到這格時已用掉多少個硬幣
class Solution:
    """
    @param n: the value from 1 - n
    @param value: the value of coins
    @param amount: the number of coins
    @return: how many different value
    """
    def backPackVIII(self, n, value, amount):
        '''
            5
            [1,2,4]
            [2,1,1]

            [1,0,0,0,0,0]
        1,2 [1,1,1,0,0,0]
        2,1 [1,1,1,1,1,0]
        4,1 [1,1,1,1,1,1]

        '''
        dp = [False for _ in range(n + 1)]
        dp[0] = True
        count = 0
        for i in range(len(value)):
            used = [0 for _ in range(n + 1)]
            for j in range(value[i], n + 1):
                if not dp[j] and dp[j - value[i]] and used[j - value[i]] < amount[i]:
                    dp[j] = 1
                    count += 1
                    used[j] = used[j - value[i]] + 1

        return count
