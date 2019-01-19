class Solution:
    """
    @param strs: the given array of strings
    @return: The anagrams which have been divided into groups
    """
    def groupAnagrams(self, strs):

        from bisect import bisect_left
        groups = {}
        for s in strs:
            key = self.lettersToKey(s)
            if key not in groups:
                groups[key] = []

            groups[key].insert(bisect_left(groups[key], s), s)

        return [v for v in groups.values()]


    def lettersToKey(self, string):
        counts = [0 for i in range(26)]
        for ch in string:
            counts[ord(ch) - ord('a')] += 1

        result = ""
        for i, v in enumerate(counts):
            if v > 0:
                result += chr(i + ord('a')) + str(v)

        return result