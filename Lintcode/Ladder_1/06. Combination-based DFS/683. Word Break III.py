# DFS, bottom up, memorized
class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        # count max length of dict word and turn dict into lowercase
        max_len = 0
        lower_dict = set()
        for word in dict:
            lower_dict.add(word.lower())
            if len(word) > max_len:
                max_len = len(word)

        return self.dfs(len(s), s.lower(), lower_dict, max_len, 0, {})


    def dfs(self, n, lower_s, lower_dict, max_len, start, records):
        if start == n:
            return 1

        if start in records:
            return records[start]

        count = 0
        for end in range(start + 1, min(n + 1, start + 1 + max_len)):
            if lower_s[start:end] in lower_dict:
                count += self.dfs(n, lower_s, lower_dict, max_len, end, records)

        records[start] = count

        return count



# Version 2: DP
class Solution:
    """
    @param: : A string
    @param: : A set of word
    @return: the number of possible sentences.
    """

    def wordBreak3(self, s, dict):
        max_len = 0
        lower_dict = set()
        for word in dict:
            lower_dict.add(word.lower())
            if len(word) > max_len:
                max_len = len(word)

        s = s.lower()
        n = len(s)

        # define f[i] as the number of combinations that s[:i - 1]
        # can be breaked into using words in dict
        '''
              C  a  t  m  a  t
            0  1  2  3  4  5  6
            1  1  1  2  1  0  3

        '''

        f = [0 for _ in range(n + 1)]

        # init
        f[0] = 1

        # function
        for end in range(1, n + 1):
            for start in range(max(end - max_len, 0), end):
                if s[start:end] in lower_dict:
                    f[end] += f[start]

        # ans
        return f[-1]