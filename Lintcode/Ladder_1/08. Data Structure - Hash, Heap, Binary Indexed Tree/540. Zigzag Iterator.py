class ZigzagIterator:
    """
    @param: v1: A 1d vector
    @param: v2: A 1d vector
    """
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2
        if len(v1) == 0:
            self.v1 = v2

    """
    @return: An integer
    """
    def next(self):
        val = self.v1[0]
        del self.v1[0]

        if len(self.v2) > 0:
            temp = self.v1
            self.v1 = self.v2
            self.v2 = temp

        return val

    """
    @return: True if has next
    """
    def hasNext(self):
        return len(self.v1) > 0


# Your ZigzagIterator object will be instantiated and called as such:
# solution, result = ZigzagIterator(v1, v2), []
# while solution.hasNext(): result.append(solution.next())
# Output result