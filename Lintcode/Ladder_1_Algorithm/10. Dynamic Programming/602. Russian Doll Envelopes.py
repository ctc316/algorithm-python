# Version 1: longest increasing subsequence + Binary Search
class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        n = len(envelopes)
        if n == 0:
            return 0

        '''
        按第一个变量升序 第二个变量降序排列
        对第二个变量做longest increasing subsequence

        更新 seq 前段是為了用小值取代大值

        [[2,3],[5,4],[6,7],[6,5],[7,8],[7,7],[7,6],[8,9]]

        length [1, 2, 3, 3, 4, 4, 4, 5]
        seq:    [6, 7, 7, 8, 9, 0, 0, 0]

        [[1,2],[2,3],[3,5],[3,4],[4,5],[5,6],[5,5],[6,7],[7,8]]

        length:[1, 2, 3, 3, 4, 5, 5, 6, 7]
        seq:   [2, 3, 5, 5, 6, 7, 8, 0, 0]

        '''
        envelopes.sort(key = lambda x: (x[0], -x[1]))
        seq = [0 for _ in range(n)]
        length = 0
        for i in range(n):
            prev = self.binarySearch(seq, length, envelopes[i][1])
            seq[prev] = envelopes[i][1]
            if prev == length:
                length += 1

        return length


    def binarySearch(self, seq, end, target):
        left = 0
        right = end
        while left + 1 < right:
            mid = int((left + right) / 2)
            if seq[mid] < target:
                left = mid
            else:
                right = mid

        if target > seq[left]:
            return right
        return left



# Version 2: DP, TLE
class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        n = len(envelopes)
        if n == 0:
            return 0

        envelopes.sort(key = lambda x: (x[0], x[1]))
        dp = [1 for _ in range(n)]
        global_max = 1
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if envelopes[j][0] < envelopes[i][0] and envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    global_max = max(global_max, dp[i])

        return global_max



# Version 3: DFS + Memorization,  TLE
class Solution:

    records = {}

    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        envelopes.sort(reverse=True)
        return self.dfs(envelopes, 0, [sys.maxsize, sys.maxsize])

    def dfs(self, envelopes, start, last_env):
        if start == len(envelopes):
            return 0

        if start in self.records:
            return self.records[start]

        maxi = 0
        for i in range(start, len(envelopes)):
            if envelopes[i][0] >= last_env[0] or envelopes[i][1] >= last_env[1]:
                continue

            maxi = max(maxi, 1 + self.dfs(envelopes, i + 1, envelopes[i]))

        self.records[start] = maxi

        return maxi