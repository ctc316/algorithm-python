class Solution:
    """
    @param paragraph:
    @param banned:
    @return: nothing
    """
    def mostCommonWord(self, paragraph, banned):
        paragraph = self.removePunctuation(paragraph.lower())
        counts = {}
        most = 0
        most_common = ""
        for word in paragraph.split():
            if word in banned:
                continue

            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1

            if counts[word] > most:
                most = counts[word]
                most_common = word

        return most_common


    def removePunctuation(self, paragraph):
        res = ""
        for p in paragraph:
            if p == " " or p >= 'a' and p <= 'z':
                res += p
        return res