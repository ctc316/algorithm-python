class Solution:
    """
    @param length: the length of board
    @param connections: the connections of the positions
    @return: the minimum steps to reach the end
    """
    def modernLudo(self, length, connections):
        
        from queue import Queue
        q = Queue()
        visited = set()
        
        q.put(0)
        visited.add(0)
        steps = 0
        
        while not q.empty():
            steps += 1
            for _ in range(q.qsize()):
                pos = q.get()
                for i in range(1, 7):
                    next = pos + i
                    if next in visited:
                        continue
                    
                    if next == length:
                        return steps
            
                    q.put(next)
                    visited.add(next)
                    
                    for conn in self.findconn(next, visited, connections):
                        if conn == length:
                            return steps
                        
                        q.put(conn)
                        visited.add(conn)
            
    
    def findconn(self, pos, visited, connections):
        results = set()
        for i in range(len(connections)):
            if connections[i][0] == pos:
                if connections[i][1] in visited:
                    continue
                
                visited.add(connections[i][1])
                results.add(connections[i][1])
                
            if connections[i][0] > pos:
                break
        
        for r in results:
            results.update(self.findconn(r, visited, connections))
            
        return list(results)
            
        