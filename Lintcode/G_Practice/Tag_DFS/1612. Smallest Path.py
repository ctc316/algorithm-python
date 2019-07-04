class Solution:
    """
    @param matrix:
    @return: Return the smallest path
    """
    def smallestPath(self, matrix):
        if not matrix:
            return

        n = len(matrix)
        m = len(matrix[0])
        sm_paths = [[float("Inf") for _ in range(m)] for _ in range(n)]
        for j in range(m):
            self.dfs(matrix, n, m, 0, j, sm_paths)

        return min(sm_paths[0])


    def dfs(self, matrix, n, m, i, j, sm_paths):
        if i == n - 1:
            sm_paths[i][j] = matrix[i][j]

        if sm_paths[i][j] != float("Inf"):
            return sm_paths[i][j]

        mini = float("Inf")
        x = i + 1
        for y in range(max(0, j - 1), min(m, j + 2)):
            mini = min(mini, self.dfs(matrix, n, m, x, y, sm_paths))

        sm_paths[i][j] = matrix[i][j] + mini
        return sm_paths[i][j]



# BFS TLE
class Solution:
    """
    @param matrix:
    @return: Return the smallest path
    """
    def smallestPath(self, matrix):
        if not matrix:
            return 0
        n = len(matrix)
        m = len(matrix[0])
        from queue import Queue
        q = Queue()
        smallest = float("Inf")
        for j in range(m):
            q.put((0, j, 0))
            while not q.empty():
                x, y, path = q.get()
                path += matrix[x][y]
                if x == n - 1:
                    smallest = min(smallest, path)
                    continue
                for nei in self.__getNeighbors(matrix, n, m, x, y):
                    q.put((nei[0], nei[1], path))

        return smallest


    def __getNeighbors(self, matrix, n, m, x, y):
        res = []
        x_ = x + 1
        for y_ in range(y - 1, y + 2):
            if x_ < 0 or x_ >= n or y_ < 0 or y_ >= m:
                continue

            res.append((x_, y_))
        return res