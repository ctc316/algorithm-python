class Solution:
    """
    @param pattern: a string, denote pattern string
    @param str: a string, denote matching string
    @return: an boolean, denote whether the pattern string and the matching string match or not
    """
    def wordPattern(self, pattern, str):
        strArr = str.split(" ")
        if len(pattern) != len(strArr):
            return False

        mapping = {}
        usedPattern = set()

        for i in range(len(strArr)):
            pat = pattern[i]
            s = strArr[i]

            # mapped
            if s in mapping:
                # not matched
                if mapping[s] != pat:
                    return False

            # mapping conflict
            elif pat in usedPattern:
                return False

            # new mapping
            else:
                usedPattern.add(pat)
                mapping[s] = pat

        return True