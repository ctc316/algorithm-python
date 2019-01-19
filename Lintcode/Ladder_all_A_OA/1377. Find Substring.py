class Solution:
    """
    @param str: The string
    @param k: The length of the substring
    @return: The answer
    """
    def findSubstring(self, str, k):
        if(k > 26):
            return 0

        ans = {}
        n = len(str)
        for i in range(0, n - k + 1):
            if(self.check(str[i : i + k])):
                ans[str[i : i + k]] = 1

        return len(ans)


    def check(self, str) :
        cnt = [0 for i in range(26)]
        for i in str:
            cnt[ord(i) - ord('a')] += 1
            if(cnt[ord(i) - ord('a')] > 1):
                return False
        return True