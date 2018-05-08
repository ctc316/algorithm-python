"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""


class Solution:
    """
    @param: nodes: a array of Undirected graph node
    @return: a connected set of a Undirected graph
    """
    def connectedSet(self, nodes):
        if len(nodes) == 0:
            return []
            
        results = []
        
        from queue import Queue
        q = Queue()
        hash = set()
        
        for node in nodes:
            if node in hash:
                continue
            
            q.put(node)
            hash.add(node)
            
            connected = []
            while not q.empty():
                curr = q.get()
                connected.append(curr.label)
                
                for nei in curr.neighbors:
                    if nei in hash:
                        continue
                    
                    q.put(nei)
                    hash.add(nei)
            
            connected.sort()
            results.append(connected)
        
        return results