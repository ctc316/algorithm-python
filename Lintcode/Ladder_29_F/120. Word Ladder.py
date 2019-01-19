class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):

        dict.add(end)

        from queue import Queue
        q = Queue()
        visited = set()

        q.put(start)
        visited.add(start)

        step = 1
        while not q.empty():
            for _ in range(q.qsize()):
                word = q.get()
                if word == end:
                    return step

                for next in self.wordTransform(word, dict):
                    if next in visited:
                        continue

                    q.put(next)
                    visited.add(next)

            step += 1


    def wordTransform(self, word, dict):
        for i in range(len(word)):
            left = word[:i]
            right = word[i + 1:]
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                new_word = left + ch + right
                if new_word in dict:
                    yield new_word