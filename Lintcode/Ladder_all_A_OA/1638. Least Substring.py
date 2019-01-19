class Solution:
    """
    @param s: the string s
    @param k: the maximum length of substring
    @return: return the least number of substring
    """
    def getAns(self, s, k):
        sub = ""
        count = 0
        for ch in s:
            if len(sub) != 0 and ch != sub[-1] or len(sub) == k:
                count += 1
                sub = ""

            sub += ch

        return count + 1