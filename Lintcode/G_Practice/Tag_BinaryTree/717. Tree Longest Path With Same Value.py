'''
We consider an undirected tree with N nodes, numbered from 1 to N,
Additionally, each node also has a label attached to it and the label is an integer value.
Note that different nodes can have identical labels. You need to write a function , that ,
given a zero-indexed array A of length N, where A[J] is the label value of the (J + 1)-th node
n the tree, and a zero-indexed array E of length K = (N - 1) * 2 in which the edges of the tree
are described (for every 0 <= j <= N -2 values E[2 * J] and E[2 * J + 1] represents and edge
connecting node E[2 * J] with node E[2 * J + 1])， returns the length of the longest path
such that all the nodes on that path have the same label.

Then length of a path if defined as the number of edges in that path.

Assume that: 1 <= N <= 1000


Example1

Input: A = [1, 1, 1 ,2, 2] and E = [1, 2, 1, 3, 2, 4, 2, 5]
Output: 2
Explanation:
described tree appears as follows:
​```
                   1 （value = 1）
                 /   \
    (value = 1) 2     3 (value = 1)
               /  \
 (value = 2)  4     5 (value = 2)
​```
The longest path (in which all nodes have the save value of 1) is (2 -> 1 -> 3). The number of edges on this path is 2, thus, that is the answer.


Example2

Input: A = [1, 2, 1 ,2, 2] and E = [1, 2, 1, 3, 2, 4, 2, 5]
Output: 2
Explanation:
described tree appears as follows:
​```
                   1 （value = 1）
                 /   \
    (value = 2) 2     3 (value = 1)
               /  \
 (value = 2)  4     5 (value = 2)
​```
The longest path (in which all nodes have the save value of 2) is (4 -> 2 -> 5). The number of edges on this path is 2, thus, that is the answer.
'''


class GraphNode:
    def __init__(self, val):
        self.val = val
        self.adjacents = set()


class Solution:
    """
    @param A: as indicated in the description
    @param E: as indicated in the description
    @return: Return the number of edges on the longest path with same value.
    """
    def LongestPathWithSameValue(self, A, E):
        if not A or len(A) == 0:
            return 0

        # init graph
        n = len(A)
        graph = {i + 1: GraphNode(A[i]) for i in range(n)}
        for i in range(0, len(E), 2):
            graph[E[i]].adjacents.add(E[i + 1])
            graph[E[i + 1]].adjacents.add(E[i])

        # recursive + divide and conquer
        visited = set()
        longest = 0
        for i, node in graph.items():
            if i in visited:
                continue

            visited.add(i)
            sub_longest, _ = self.findLongestByNode(i, graph, visited)
            longest = max(longest, sub_longest)

        return longest - 1


    def findLongestByNode(self, i, graph, visited):
        con_longest1 = 0
        con_longest2 = 0
        longest = 0
        for adj in graph[i].adjacents:
            if adj in visited or graph[adj].val != graph[i].val:
                continue

            visited.add(adj)
            sub_longest, con_longest = self.findLongestByNode(adj, graph, visited)
            longest = max(longest, sub_longest)
            if con_longest > con_longest1:
                con_longest2 = con_longest1
                con_longest1 = con_longest
            elif con_longest > con_longest2:
                con_longest2 = con_longest

        return max(longest, con_longest1 + con_longest2 + 1), con_longest1 + 1