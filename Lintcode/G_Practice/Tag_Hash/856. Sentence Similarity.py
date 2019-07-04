class Solution:
    """
    @param words1: a list of string
    @param words2: a list of string
    @param pairs: a list of string pairs
    @return: return a boolean, denote whether two sentences are similar or not
    """
    def isSentenceSimilarity(self, words1, words2, pairs):
        if len(words1) != len(words2):
            return False

        sims = {}
        for p in pairs:
            if p[0] not in sims:
                sims[p[0]] = set()
            sims[p[0]].update([p[0], p[1]])

            if p[1] not in sims:
                sims[p[1]] = set()
            sims[p[1]].update([p[0], p[1]])

        for i, w in enumerate(words1):
            if w not in sims or words2[i] not in sims[w]:
                return False

        return True
