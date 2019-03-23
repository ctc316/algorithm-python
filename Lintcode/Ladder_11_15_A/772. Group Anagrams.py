class Solution:
    """
    @param strs: the given array of strings
    @return: The anagrams which have been divided into groups
    """
    def groupAnagrams(self, strs):
        from bisect import bisect_left
        groups = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in groups:
                groups[key] = []

            groups[key].insert(bisect_left(groups[key], s), s)

        return [v for v in groups.values()]