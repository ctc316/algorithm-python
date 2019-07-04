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
        sLen = len(source)
        if tLen == 0:
            return 0

        HASH_KEY = 31
        HASH_SIZE = 100000

        t_hash = 0  # hash of target
        maxPow = 1  # value of max power for substraction
        for ch in target:
            t_hash = (t_hash * HASH_KEY + ord(ch)) % HASH_SIZE
            maxPow = (maxPow * HASH_KEY) % HASH_SIZE;

        # hash of source & compare
        s_hash = 0
        for i in range(sLen):
            s_hash = (s_hash * HASH_KEY + ord(source[i])) % HASH_SIZE
            if i < tLen - 1:
                continue

            if i >= tLen:
                s_hash = s_hash - (ord(source[i - tLen]) * maxPow) % HASH_SIZE;
                if s_hash < 0:
                    s_hash += HASH_SIZE

            if s_hash == t_hash:
                start = i - tLen + 1
                if source[start:i + 1] == target:
                    return start

        return -1