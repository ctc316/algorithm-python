class Solution:
    """
    @param flowers: an array
    @param k: an integer
    @param m: an integer
    @return: the last day
    """
    def flowerProblem(self, flowers, k, m):
        n = len(flowers)
        if n == 0:
            return -1
        if k <= 1:
            return m

        self.father = [i for i in range(n + 1)]
        self.counts = [0 for i in range(n + 1)]
        self.m_count = 0
        self.k = k

        lastday = -1
        for i in range(n):
            pos = flowers[i]

            # add
            self.counts[pos] = 1

            # union
            if pos + 1 <= n and self.counts[pos + 1] > 0:
                self.__union(pos, pos + 1)
            if pos - 1 > 0 and self.counts[pos - 1] > 0:
                self.__union(pos, pos - 1)

            # check
            if self.m_count >= m:
                lastday = i + 1

        return lastday


    def __find(self, pos):
        path = []
        while pos != self.father[pos]:
            path.append(pos)
            pos = self.father[pos]

        for p in path:
            self.father[p] = pos

        return pos


    def __union(self, pos, target):
        fa1 = self.__find(pos)
        fa2 = self.__find(target)
        if fa1 != fa2:
            self.father[fa1] = fa2

            if self.counts[fa1] >= self.k:
                self.m_count -= 1
            if self.counts[fa2] < self.k and self.counts[fa2] + self.counts[fa1] >= self.k:
                self.m_count += 1

            self.counts[fa2] += self.counts[fa1]