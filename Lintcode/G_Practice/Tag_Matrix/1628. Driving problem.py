class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n + 2)]
    
    def find(self, a):
        path = []
        while self.parent[a] != a:
            path.append(a)
            a = self.parent[a]
        
        for p in path:
            self.parent[p] = a
        
        return a
        
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_b] = root_a
            

class Solution:
    """
    @param L: the length
    @param W: the width
    @param p:  the obstacle coordinates
    @return: yes or no
    """
    def drivingProblem(self, L, W, p):
        '''
        0 1 0 0 0 0 0 0 0 0
        1 1 1 0 0 0 0 0 0 0
        0 1 0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0 0 0
        0 0 0 0 0 0 0 0 0 0
        0 0 0 0 0 0 1 0 0 0
        0 0 0 0 0 1 1 1 0 0
        0 0 0 0 0 0 1 0 0 0
        0 0 0 0 0 0 0 0 0 0
        是否可以从路的一侧通过不断连接路障到达路的另一侧, 并且每个连接的距离都小于车的直径+路障的直径 (在连接路沿和路障时, 距离limit为车的直径和路障的半径
        '''
        n = len(p)
        union = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                dx = abs(p[i][0] - p[j][0])
                dy = abs(p[i][1] - p[j][1])
                if dx + dy <= 6:
                    union.union(i, j)
                    
            # edge
            if p[i][1] <= 5:
                union.union(i, n)
            if W - p[i][1] <= 5:
                union.union(i, n + 1)
        
        return "no" if union.find(n) == union.find(n + 1) else "yes"
    
    