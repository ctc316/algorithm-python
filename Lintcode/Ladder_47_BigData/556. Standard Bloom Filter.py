class HashFunc:
    def __init__(self, capacity, seed):
        self.capacity = capacity
        self.seed = seed

    def hash(self, word):
        ret = 0
        for ch in word:
            ret = (ret * self.seed + ord(ch)) % self.capacity

        return ret


class StandardBloomFilter:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.bitset = dict()
        self.hashFuncs = []
        for i in range(k):
            self.hashFuncs.append(HashFunc(20000, 30 + i * 2 + 3))


    """
    @param: word: A string
    @return: nothing
    """
    def add(self, word):
        for f in self.hashFuncs:
            self.bitset[f.hash(word)] = 1

    """
    @param: word: A string
    @return: True if contains word
    """
    def contains(self, word):
        for f in self.hashFuncs:
            if f.hash(word) not in self.bitset:
                return False

        return True