class Solution:
    """
    @param s: the string
    @param k: the k
    @return: the answer
    """
    def wordSegmentation(self, s, k):
        res = []
        i = 0
        words = s.split(" ")
        n = len(words)
        while i < n:
            line = words[i]
            j = i + 1
            while j < n:
                if len(line) + len(words[j]) < k:
                    line += " " + words[j]
                    j += 1
                else:
                    break

            res.append(line)
            i = j

        return res