class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt_s = {}
        for ch in s:
            cnt_s[ch] = cnt_s.get(ch, 0) + 1

        for ch in t:
            if ch not in cnt_s:
                return False
            cnt_s[ch] -= 1
            if cnt_s[ch] == 0:
                del cnt_s[ch]

        return len(cnt_s) == 0