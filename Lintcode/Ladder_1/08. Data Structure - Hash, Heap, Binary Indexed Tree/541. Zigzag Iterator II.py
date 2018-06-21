class ZigzagIterator2:
    """
    @param: vecs: a list of 1d vectors
    """
    def __init__(self, vecs):
        self.vecs = vecs
        self.pointer = 0
        i = 0
        while i < len(vecs):
            if len(vecs[i]) == 0:
                del vecs[i]
            else:
                i += 1

    """
    @return: An integer
    """
    def next(self):
        val = self.vecs[self.pointer][0]
        del self.vecs[self.pointer][0]

        if len(self.vecs[self.pointer]) == 0:
            del self.vecs[self.pointer]
        else:
            self.pointer += 1

        if len(self.vecs) > 0:
            self.pointer %= len(self.vecs)

        return val

    """
    @return: True if has next
    """
    def hasNext(self):
        return len(self.vecs) > 0

# Your ZigzagIterator2 object will be instantiated and called as such:
# solution, result = ZigzagIterator2(vecs), []
# while solution.hasNext(): result.append(solution.next())
# Output result