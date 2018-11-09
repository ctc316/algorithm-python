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
        self.m_count = 0
        self.k = k
        lastday = -1
        for i in range(n):
            pos = flowers[i]

            # add
            self.groups[pos] = 1
            if k == 1:
                self.m_count += 1

            # union
            if pos + 1 <= n and self.find(pos + 1) in self.groups:
                self.union(pos, pos + 1)

            if pos - 1 > 0 and self.find(pos - 1) in self.groups:
                self.union(pos, pos - 1)

            if self.m_count >= m:
                lastday = i + 1

        return lastday


    def find(self, pos):
        # find root
        path = []
        while pos != self.father[pos]:
            path.append(pos)
            pos = self.father[pos]

        # compress
        for p in path:
            self.father[p] = pos

        return pos


    def union(self, pos, target):
        fa1 = self.find(pos)
        fa2 = self.find(target)
        if fa1 != fa2:
            self.father[fa1] = fa2

            if self.groups[fa1] >= self.k:
                self.m_count -= 1
            if self.groups[fa2] < self.k and self.groups[fa2] + self.groups[fa1] >= self.k:
                self.m_count += 1

            self.groups[fa2] += self.groups[fa1]
            del self.groups[fa1]