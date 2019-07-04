"""
The read4 API is already defined for you.
@param buf a list of characters
@return an integer
you can call Reader.read4(buf)
"""


class Solution:

    def __init__(self):
        self.buf4, self.idx, self.len4 = [None] * 4, 0, 0

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        i = 0
        while i < n:
            if self.idx == self.len4:
                self.idx, self.len4 = 0, Reader.read4(self.buf4)
                if not self.len4:
                    break
            buf[i] = self.buf4[self.idx]
            i += 1
            self.idx += 1
        return i