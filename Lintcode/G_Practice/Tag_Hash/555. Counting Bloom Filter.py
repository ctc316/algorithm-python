class HashFunc:
    def __init__(self, capacity, seed):
        self.capacity = capacity
        self.seed = seed

    def hash(self, word):
        res = 0
        for ch in word:
            res = (res * self.seed + ord(ch)) % self.capacity
        return res


class CountingBloomFilter:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        size = 20000
        self.hashFuncs = [HashFunc(size, 37 + i * 2) for i in range(k)]
        self.countSet = [0 for _ in range(size)]


    """
    @param: word: A string
    @return: nothing
    """
    def add(self, word):
        for f in self.hashFuncs:
            self.countSet[f.hash(word)] += 1

    """
    @param: word: A string
    @return: nothing
    """
    def remove(self, word):
        for f in self.hashFuncs:
            self.countSet[f.hash(word)] -= 1

    """
    @param: word: A string
    @return: True if contains word
    """
    def contains(self, word):
        for f in self.hashFuncs:
            if self.countSet[f.hash(word)] <= 0:
                return False
        return True
