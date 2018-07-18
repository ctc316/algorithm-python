#
class Solution:

    records = {} # {idx: {remain: count}}

    """
    @param N: The number of integers
    @return: The number of beautiful arrangements you can construct
    """
    def countArrangement(self, N):
        '''
            N=1: [1]
            N=2: [1,2],[2,1]
            N=3: [1,2,3],[2,1,3][3,2,1]
            N=4: [1,2,3,4],[2,1,3,4][3,2,1,4]
                 [4,2,3,1][4,1,3,2]
                 [1,4,3,2][2,4,3,1][3,4,1,2]
        '''

        return self.dfs(N, 1, [i for i in range(1, N + 1)])


    def dfs(self, N, idx, remain):
        if idx > N:
            return 1

        key = self.getKey(remain)
        if idx in self.records and key in self.records[idx]:
            return self.records[idx][key]

        count = 0
        for i in range(len(remain)):
            num = remain[i]
            if num % idx == 0 or idx % num == 0:
                remain.pop(i)
                count += self.dfs(N, idx + 1, remain)
                remain.insert(i, num)


        if idx not in self.records:
            self.records[idx] = {}

        self.records[idx][key] = count

        return count


    def getKey(self, remain):
        key = ""
        for r in remain:
            key += str(r) + "_"
        return key