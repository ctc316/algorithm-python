# Version 1: DFS (Recursion), Stack Overflow
class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        return self.dfs(s, 0, dict)

    def dfs(self, s, start, dict):
        if start >= len(s):
            return True

        for end in range(start, len(s) + 1):
            word = s[start:end]
            if word in dict and self.dfs(s, end, dict):
                return True

        return False


# Version 2: BFS, Time Limit Exceeded
class Solution:
    """
    @param: s: A string
    @param: dict: A dictionary of words dict
    @return: A boolean
    """
    def wordBreak(self, s, dict):
        n = len(s)
        if n == 0:
            return True

        # get max length in dict
        maxLength = 0
        for d in dict:
            maxLength = max(len(d), maxLength)
        if maxLength == 0:
            return False

        # BFS
        from queue import Queue
        q = Queue()
        hash = set()

        q.put(0)
        hash.add(0)

        while q.qsize() > 0:
            start = q.get()
            for end in range(start + 1, min(start + 1 + maxLength, n + 1)):
                if end in hash:
                    continue

                if s[start:end] in dict:
                    if end == n:
                        return True
                    q.put(end)
                    hash.add(end)

        return False