class Solution:
    
    MOVES = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    n = 0
    m = 0
    
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        if len(word) == 0:
            return True
            
        if len(board) == 0 or len(board[0]) == 0:
            return False
        
        self.n = len(board)
        self.m = len(board[0])
        visited = [[False for j in range(self.m)] for i in range(self.n)]
        
        for i in range(self.n):
            for j in range(self.m):
                if board[i][j] != word[0]:
                    continue
                
                visited[i][j] = True
                if self.dfs(board, word, i, j, board[i][j], visited):
                    return True
                visited[i][j] = False
        
        return False
        
    
    def dfs(self, board, word, row, col, str, visited):
        if str == word:
            return True
    
        if len(str) == len(word):
            return False
        
        nextCh = word[len(str)]
        
        for move in self.MOVES:
            row_ = row + move[0]
            col_ = col + move[1]
            
            if row_ < 0 or row_ >= self.n or col_ < 0 or col_ >= self.m:
                continue
            
            if visited[row_][col_]:
                continue
            
            if board[row_][col_] == nextCh:
                visited[row_][col_] = True
                if self.dfs(board, word, row_, col_, str + nextCh, visited):
                    return True
                visited[row_][col_] = False
        
        return False
