# Version 1: Bruteforce, Time: O(n * m^2), Space: O(1), Fail in submission
class Solution:
    """
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer
    """
    def stringReplace(self, a, b, s):
        result = ""
        start = 0
        while start < len(s):
            found = False
            for end in range(len(s), start + 1, -1):
                str = s[start : end]
                if str in a:
                    result += b[a.index(str)]
                    found = True
                    start = end
                    break

            if not found:
                result += s[start]
                start += 1

        return result


# Version 2: Bruteforce with optimization, time: O(s * aloga), Space: O(n), Accepted (Sometimes Fails)
class Solution:
    """
    @param a: The A array
    @param b: The B array
    @param s: The S string
    @return: The answer
    """
    def stringReplace(self, a, b, s):

        # find length options of replacement strings in a[] and construct idx map
        repLens = set()
        idxMap = {}
        for i in range(len(a)):
            repLens.add(len(a[i]))
            idxMap[a[i]] = i

        repLens = sorted(repLens, reverse=True)

        # find replacements
        result = ""
        start = 0
        while start < len(s):
            found = False
            for replen in repLens:
                end = start + replen
                if end > len(s):
                    continue

                str = s[start : end]
                if str in a:
                    result += b[idxMap.get(str)]
                    found = True
                    start = end
                    break

            if not found:
                result += s[start]
                start += 1

        return result