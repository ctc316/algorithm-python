# Rabin Karp, Time: O(n + m), Space: O(1)
class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """
    def strStr2(self, source, target):
        if source is None or target is None:
            return -1

        tLen = len(target)
        if tLen == 0:
            return 0

        HASH_KEY = 31
        HASH_SIZE = 100000

        # hash of target
        t_hash = 0
        for ch in target:
            t_hash = (ord(ch) + t_hash * HASH_KEY) % HASH_SIZE


        # calculate key ^ tLen for the minus action
        maxPow = 1;
        for i in range(tLen):
            maxPow = (maxPow * HASH_KEY) % HASH_SIZE;


        # hash of source & compare
        s_hash = 0
        for i in range(len(source)):
            s_hash = (ord(source[i]) + s_hash * HASH_KEY) % HASH_SIZE

            if i < tLen - 1:
                continue

            if i >= tLen:
                s_hash = s_hash - (ord(source[i - tLen]) * maxPow) % HASH_SIZE;
                if s_hash < 0:
                    s_hash += HASH_SIZE

            if s_hash == t_hash:
                start = i - tLen + 1
                if source[start : i + 1] == target:
                    return start

        return -1