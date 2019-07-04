class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_cnts = {}
        for ch in s1:
            if ch not in s1_cnts:
                s1_cnts[ch] = 1
            else:
                s1_cnts[ch] += 1

        s1_len = len(s1)
        s2_cnts = [0 for _ in range(26)]
        for i in range(len(s2)):
            if i >= s1_len:
                s2_cnts[ord(s2[i - s1_len]) - ord('a')] -= 1

            s2_cnts[ord(s2[i]) - ord('a')] += 1

            if i >= s1_len - 1:
                matched = True
                for k, v in s1_cnts.items():
                    if v != s2_cnts[ord(k) - ord('a')]:
                        matched = False
                        break

                if matched:
                    return True

        return False


