# Version 1: DP
class Solution:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def canCross(self, stones):
        dp = {} # stone, lastjumps
        for stone in stones:
            dp[stone] = set([])

        dp[0].add(0)

        for stone in stones:
            for k in dp[stone]:
                for jump in (k - 1, k, k + 1):
                    if jump > 0 and stone + jump in dp:
                        dp[stone + jump].add(jump)

        return len(dp[stones[-1]]) > 0
        


# Version 2: BFS
class Solution:
    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def canCross(self, stones):
        if not stones:
            return False

        hash = set(stones)  # x in set is O(1)

        from queue import Queue
        q = Queue()
        q.put((stones[0], 0))
        visited = {(stones[0], 0): True}

        while not q.empty():
            pos, lastjump = q.get()
            if pos == stones[-1]:
                return True

            for jump in (lastjump - 1, lastjump, lastjump + 1):
                if pos + jump in hash and not visited.get((pos + jump, jump)):
                    visited[pos + jump, jump] = True
                    q.put((pos + jump, jump))

        return False




# Version 3: DFS + Memorization, TLE
class Solution:

    records = {}

    """
    @param stones: a list of stones' positions in sorted ascending order
    @return: true if the frog is able to cross the river or false
    """
    def canCross(self, stones):
        n = len(stones)
        if n == 0:
            return False

        return self.dfs(stones, 0, 1, 0)


    def dfs(self, stones, position, start, lastjump):
        if start == len(stones):
            return True

        hashkey = str(position) + "_" + str(lastjump)
        if hashkey in  self.records:
            return self.records[hashkey]

        for i in range(start, len(stones)):
            for j in range(-1, 2):
                jumpTo = position + lastjump + j
                for k in range(i, len(stones)):
                    if jumpTo < stones[k]:
                        break

                    if jumpTo == stones[k]:
                        res = self.dfs(stones, jumpTo, k + 1, lastjump + j)
                        if res is True:
                            return True


        self.records[hashkey] = False

        return False