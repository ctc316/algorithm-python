class Solution:
    """
    @param stringIn: The original string.
    @param K: The length of substrings.
    @return: return the count of substring of length K and exactly K distinct characters.
    """
    def KSubstring(self, stringIn, K):
        ch_cnt = {}
        diff_chs = 0
        records = set()
        for i in range(len(stringIn)):
            if stringIn[i] not in ch_cnt:
                ch_cnt[stringIn[i]] = 1
            else:
                ch_cnt[stringIn[i]] += 1
            if ch_cnt[stringIn[i]] == 1:
                diff_chs += 1

            if i >= K:
                ch_cnt[stringIn[i - K]] -= 1
                if ch_cnt[stringIn[i - K]] == 0:
                    diff_chs -= 1

            if i >= K - 1 and diff_chs == K:
                records.add(stringIn[i - K: i + 1])

        return len(records)