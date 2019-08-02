class Solution:
    """
    @param M: a matrix
    @return: the total number of friend circles among all the students
    """
    def findCircleNum(self, M):
        if not M or not M[0]:
            return 0

        n = len(M)
        dir_friends = {i:[] for i in range(n)}
        for i in range(n):
            for j in range(i + 1, n):
                if M[i][j] == 1:
                    dir_friends[i].append(j)
                    dir_friends[j].append(i)

        visited = set()
        circles = 0
        for i in range(n):
            if i in visited:
                continue
            circles += 1
            self.bfs(dir_friends, i, visited)

        return circles


    def bfs(self, edges, start, visited):
        from queue import Queue
        q = Queue()
        q.put(start)
        visited.add(start)
        while not q.empty():
            node = q.get()
            for next in edges[node]:
                if next in visited:
                    continue
                visited.add(next)
                q.put(next)