class Solution:
    """
    @param s: The data stream
    @return: Return the judgement stream
    """
    def getStream(self, s):
        alphabet_cnt = [0 for _ in range(26)]
        results = []
        odd_cnt = 0
        for ch in s:
            alphabet_cnt[ord(ch) - ord('a')] += 1
            if alphabet_cnt[ord(ch) - ord('a')] % 2 == 0:
                odd_cnt -= 1
            else:
                odd_cnt += 1

            if odd_cnt > 1:
                results.append(0)
            else:
                results.append(1)

        return results