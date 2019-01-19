class Solution:
    """
    @param matrix: 
    @param x: 
    @param y: 
    @return: return the matrix
    """
    '''
    [[1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1],
     [1,1,0,1,0,1,1]]
     
     
     [[1,1,1,1,1,1,1],
      [1,0,1,1,1,1,1],
      [1,0,1,1,1,1,1],
      [1,0,1,1,1,1,1],
      [1,0,1,1,1,1,1],
      [1,0,1,1,1,1,1],
      [1,0,0,1,0,1,1]]
    '''
    
    def removeOne(self, matrix, x, y):
        for i in range(x, len(matrix)):
            matrix[i][y] = 0
        return matrix




## 考慮左右連接
class Solution:
    """
    @param matrix: 
    @param x: 
    @param y: 
    @return: return the matrix
    """    
    def removeOne(self, matrix, x, y):
        self.n = len(matrix)
        self.m = len(matrix[0]) if matrix[0] else 0
        matrix[x][y] = 0
        visited = set()
        for pos in self.get_next_pos(matrix, visited, x, y):
            for flip in self.bfs(matrix, visited, pos[0], pos[1]):
                matrix[flip[0]][flip[1]] = 0
        
        return matrix
            
    
    def bfs(self, matrix, visited, x, y):
        if matrix[x][y] == 0 or (x, y) in visited:
            return False
        
        from queue import Queue
        q = Queue()
        visited = set()
        
        q.put((x, y))
        visited.add((x, y))
        res = [(x, y)]
        while not q.empty(): 
            x, y = q.get()
            if x == 0:
                return []
            
            for next in self.get_next_pos(matrix, visited, x, y):
                q.put(next)
                visited.add(next)
                res.append(next)
        
        return res
        
        
    def get_next_pos(self, matrix, visited, x, y):
        res = []
        for move in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                x_ = x + move[0]
                y_ = y + move[1]
                
                if x_ < 0 or x_ >= self.n or y_ < 0 or y_ >= self.m:
                    continue
                
                if (x_, y_) in visited:
                    continue
                
                if matrix[x_][y_] == 0:
                    continue
                
                res.append((x_, y_))
                
        return res