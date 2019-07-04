class Solution:
    """
    @param A: A string
    @param B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        char_cnt = {}
        for a in A:
            if a not in char_cnt:
                char_cnt[a] = 1
            else:
                char_cnt[a] += 1

        for b in B:
            if b not in char_cnt or char_cnt[b] == 0:
                return False
            char_cnt[b] -= 1

        return True