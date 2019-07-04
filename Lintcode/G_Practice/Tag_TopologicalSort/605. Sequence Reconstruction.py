class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        neighbors = collections.defaultdict(set)
        indegrees = collections.defaultdict(int)
        for s in seqs:
            if s and s[0] not in indegrees:
                indegrees[s[0]] = 0
            for i in range(1, len(s)):
                if s[i] in neighbors[s[i - 1]]:
                    continue
                neighbors[s[i - 1]].add(s[i])
                indegrees[s[i]] += 1

        from queue import Queue
        q = Queue()
        for node, ind in indegrees.items():
            if ind == 0:
                q.put(node)

        result = []
        while q.qsize() == 1:
            node = q.get()
            result.append(node)
            for next in neighbors[node]:
                indegrees[next] -= 1
                if indegrees[next] == 0:
                    q.put(next)

        return result == org
