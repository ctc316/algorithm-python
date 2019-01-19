class Solution:
    """
    @param s: the long string
    @param word: the secrect word
    @return: whether a substring exists in the string can be transformed by the above encoding rule
    """
    def getAns(self, s, word):
        n = len(s)
        m = len(word)

        last_idx = {}
        prev_ch_idx = [i for i in range(m)]
        for i in range(m):
            if word[i] in last_idx:
                prev_ch_idx[i] = last_idx[word[i]]

            last_idx[word[i]] = i


        for start in range(n - m + 1):
            end = start + m
            last_idx = {}
            for i in range(start, end):
                ch = s[i]
                idx = i - start
                if s[i] in last_idx:
                    if last_idx[ch] != prev_ch_idx[idx]:
                        break
                elif prev_ch_idx[idx] != idx:
                    break

                last_idx[ch] = idx

                if i == end - 1:
                    return 'yes'

        return 'no'