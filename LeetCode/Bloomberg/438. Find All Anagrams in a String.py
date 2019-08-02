class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        p_hash = {}
        s_hash = {}

        ans = []
        for i in range(len(p)):
            p_hash[p[i]] = p_hash.get(p[i],0) + 1
            s_hash[s[i]] = s_hash.get(s[i],0) + 1

        if s_hash == p_hash:
            ans.append(0)

        for start in range(1, len(s) - len(p) + 1):
            end = start + len(p) - 1
            s_hash[s[end]] = s_hash.get(s[end], 0) + 1
            s_hash[s[start - 1]] -= 1
            if s_hash[s[start -1]] == 0:
                del s_hash[s[start -1]]

            if s_hash == p_hash:
                ans.append(start)

        return ans