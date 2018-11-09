class ConnectingGraph:
    """
    @param: n: An integer
    """
    def __init__(self, n):
        self.fathers = [i for i in range(n + 1)]

    """
    @param: a: An integer
    @param: b: An integer
    @return: nothing
    """
    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.fathers[root_a] = root_b


    """
    @param: a: An integer
    @param: b: An integer
    @return: A boolean
    """
    def query(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        return root_a == root_b


    def find(self, a):
        # find root
        root = self.fathers[a]
        while root != self.fathers[root]:
            root = self.fathers[root]

        # compress
        while self.fathers[a] != root:
            father = self.fathers[a]
            self.fathers[a] = root
            a = root

        return root
