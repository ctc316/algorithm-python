# Version 1: Binary Search, add: O(logk), topk: O(k)
class Entry:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        self.inTop = False

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq


from bisect import bisect_left

class TopK:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.k = k
        self.top_k = []
        self.mapping = {}

    """
    @param: word: A string
    @return: nothing
    """
    def add(self, word):
        if self.k == 0:
            return

        entry = None
        if word in self.mapping:
            entry = self.mapping[word]
            if entry.inTop:
                self.removeFromTop(entry)
            entry.freq += 1
        else:
            self.mapping[word] = Entry(word, 1)
            entry = self.mapping[word]

        self.addToTop(entry)

        if len(self.top_k) > self.k:
            self.top_k[0].inTop = False
            self.top_k.pop(0)


    """
    @return: the current top k frequent words.
    """
    def topk(self):
        if self.k == 0 or len(self.top_k) == 0:
            return []

        results = [e.word for e in self.top_k]
        results.reverse()
        return results


    def addToTop(self, entry):
        idx = bisect_left(self.top_k, entry)
        self.top_k.insert(idx, entry)
        entry.inTop = True


    def removeFromTop(self, entry):
        idx = bisect_left(self.top_k, entry)
        self.top_k.pop(idx)
        entry.inTop = False






# Version 2: sort,  TLE
class Entry:
    def __init__(self, word, freq):
        self.word = word
        self.freq = freq
        self.inTop = False

    def __lt__(self, other):
        return self.freq < other.freq or \
               self.freq == other.freq and self.word > other.word

class TopK:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.pq = []
        self.k = k
        self.mapping = {}


    """
    @param: word: A string
    @return: nothing
    """
    def add(self, word):
        if self.k == 0:
            return

        theEntry = None
        if word in self.mapping:
            theEntry = self.mapping[word]
            theEntry.freq += 1
        else:
            theEntry = Entry(word, 1)
            self.mapping[word] = theEntry


        if not theEntry.inTop:
            if len(self.pq) < self.k:
                self.pq.append(theEntry)
                theEntry.inTop = True
            else:
                if theEntry < self.pq[0]:
                    return

                self.pq[0].inTop = False
                self.pq[0] = theEntry
                theEntry.inTop = True


        self.pq.sort()


    """
    @return: the current top k frequent words.
    """
    def topk(self):
        if self.k == 0:
            return []

        results = []
        for entry in self.pq:
            results.append(entry.word)
        results.reverse()
        return results