class Solution:
    """
    @param flowers: an array
    @param k: an integer
    @param m: an integer
    @return: the last day
    """
    def flowerProblem(self, flowers, k, m):
        n = len(flowers)
        self.father = [i for i in range(n + 1)]
        self.groups = {}  # root: count
        for i in range(n):
            pos = flowers[i]
            # add
            self.groups[pos] = 1
            
            # union
            if pos + 1 <= n and self.find(pos + 1) in self.groups:
                self.union(pos, pos + 1)
            
            if pos - 1 > 0 and self.find(pos - 1) in self.groups:
                self.union(pos, pos - 1)
            
            # check
            count = 0
            for val in self.groups.values():
                if val >= k:
                    count += 1
            
            if count >= m:
                return i
        
        return -1
            
    
    
    def find(self, pos):
        if self.father[pos] == pos:
            return pos
        
        # find root
        root = self.father[pos]
        while root != self.father[root]:
            root = self.father[root]
            
        # compress
        temp = -1
        while pos != self.father[pos]:
            temp = self.father[pos]
            self.father[pos] = root
            pos = temp
        
        return root
        
    
    def union(self, pos, target):
        fa1 = self.find(pos)
        fa2 = self.find(target)
        if fa1 != fa2:
            self.father[fa1] = fa2
            self.groups[fa2] += self.groups[fa1]
            del self.groups[fa1]