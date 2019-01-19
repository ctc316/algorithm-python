class GraphNode:
    def __init__(self, val):
        self.val = val
        self.neighbors = set()
        self.inDegree = 0

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        graph, startNodes = self.initGraphByWords(words)

        from queue import PriorityQueue
        pq = PriorityQueue()
        for s in startNodes:
            pq.put(s)

        result = ''
        while not pq.empty():
            node = pq.get()
            result += node.val
            for nei in list(node.neighbors):
                nei.inDegree -= 1
                if nei.inDegree == 0:
                    pq.put(nei)

        if len(result) != len(graph):
            return ''

        return result


    def initGraphByWords(self, words):
        graph = {}
        startNodes = set()

        # nodes
        for word in words:
            for ch in word:
                if ch not in graph:
                    graph[ch] = GraphNode(ch)
                    startNodes.add(graph[ch])

        # edges
        for i in range(0, len(words) - 1):
            word1 = words[i]
            word2 = words[i + 1]

            pos = 0
            while pos < len(word2) and word1[pos] == word2[pos]:
                pos += 1

            if pos >= len(word2):
                continue

            node1 = graph[word1[pos]]
            node2 = graph[word2[pos]]

            if node2 in node1.neighbors:
                continue

            node1.neighbors.add(node2)
            node2.inDegree += 1
            if node2 in startNodes:
                startNodes.remove(node2)

        return graph, list(startNodes)