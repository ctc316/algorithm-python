"""
Definition for Undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: graph: a list of Undirected graph node
    @param: s: Undirected graph node
    @param: t: Undirected graph nodes
    @return: an integer
    """
    def sixDegrees(self, graph, s, t):

        from queue import Queue
        q = Queue()
        hash = set()

        q.put(s)
        hash.add(s)

        distance = 0
        while not q.empty():
            for i in range(q.qsize()):
                node = q.get()
                if node is t:
                    return distance

                for nei in node.neighbors:
                    if nei in hash:
                        continue

                    q.put(nei)
                    hash.add(nei)

            distance += 1

        return -1