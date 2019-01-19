 class Solution:
    """
    @param s: a string
    @param excludewords: a dict
    @return: the most frequent word
    """
    def frequentWord(self, s, excludewords):
        arr = s.replace(",", "").split(" ")
        counts = {}
        for word in arr:
            if word in excludewords:
                continue

            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

        from queue import PriorityQueue
        pq = PriorityQueue()
        for k, v in counts.items():
            pq.put((-v, k))

        return pq.get()[1]