class ConnectingGraph3:
    
    def __init__(self, n):
        self.fathers = [i for i in range(n + 1)]
        self.num_roots = n
        
    
    """
    @param a: An integer
    @param b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        
        if root_a != root_b:
            self.fathers[root_a] = root_b
            self.num_roots -= 1

    """
    @return: An integer
    """
    def query(self):
        return self.num_roots
        
    
    def find(self, a):
        root = a
        path = []
        while root != self.fathers[root]:
            path.append(root)
            root = self.fathers[root]
            
        # compress
        for p in path:
            self.fathers[p] = root
        
        return root