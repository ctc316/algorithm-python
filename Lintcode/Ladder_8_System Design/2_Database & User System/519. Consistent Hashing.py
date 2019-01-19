class Solution:
    """
    @param: n: a positive integer
    @return: n x 3 matrix
    """
    def consistentHashing(self, n):
        if n == 0:
            return []
            
        shards = [[0, 359, 1]]
        for i in range(2, n + 1):
            idx = self.findMaxIntv(shards)
            toSplit = shards[idx]
            mid = (toSplit[0] + toSplit[1]) // 2
            shards.insert(idx + 1, [toSplit[0], mid, toSplit[2]])
            shards.insert(idx + 2, [mid + 1, toSplit[1], i])
            del shards[idx]
            
        return shards
        
    
    def findMaxIntv(self, shards):
        maxIdx = -1
        maxIntv = 0
        for i in range(len(shards)):
            intv = shards[i][1] - shards[i][0]
            if intv > maxIntv or intv == maxIntv and shards[i][2] < shards[maxIdx][2]:
                maxIntv = intv
                maxIdx = i
                
        return maxIdx