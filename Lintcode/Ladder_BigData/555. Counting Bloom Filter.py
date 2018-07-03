class HashFunc:
    def __init__(self, capacity, seed):
        self.capacity = capacity
        self.seed = seed

    def hash(self, word):
        result = 0
        for ch in word:
            result = (result * self.seed + ord(ch)) % self.capacity
        return result


class CountingBloomFilter:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.counts = {}
        self.hashFuncs = []
        for i in range(k):
            self.hashFuncs.append(HashFunc(20000, 30 + 2 * i + 3))


    """
    @param: word: A string
    @return: nothing
    """
    def add(self, word):
        for f in self.hashFuncs:
            key = f.hash(word)
            if key in self.counts:
                self.counts[key] += 1
            else:
                self.counts[key] = 1

    """
    @param: word: A string
    @return: nothing
    """
    def remove(self, word):
        for f in self.hashFuncs:
            key = f.hash(word)
            if key in self.counts:
                self.counts[key] -= 1
                if self.counts[key] == 0:
                    del self.counts[key]

    """
    @param: word: A string
    @return: True if contains word
    """
    def contains(self, word):
        for f in self.hashFuncs:
            key = f.hash(word)
            if key not in self.counts:
                return False

        return True