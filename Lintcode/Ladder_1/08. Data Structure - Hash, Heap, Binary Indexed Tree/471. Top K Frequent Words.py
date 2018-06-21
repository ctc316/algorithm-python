class PQEntry:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __lt__(self, other):
        return self.freq < other.freq or \
               self.freq == other.freq and self.word > other.word


class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        freq = {}
        for word in words:
            if word not in freq:
                freq[word] = 1
            else:
                freq[word] += 1


        from queue import PriorityQueue
        pq = PriorityQueue()

        for key, val in freq.items():
            pq.put(PQEntry(val, key))
            if pq.qsize() > k:
                pq.get()

        results = []
        for _ in range(k):
            results.append(pq.get().word)

        results.reverse()

        return results
