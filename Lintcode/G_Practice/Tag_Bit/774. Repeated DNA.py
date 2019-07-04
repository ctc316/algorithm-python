class Solution:
    """
    @param s: a string represent DNA sequences
    @return: all the 10-letter-long sequences
    """
    def findRepeatedDna(self, s):
        '''
        A:00, C:01, G:10, T:11
        '''
        if len(s) < 11:
            return []

        hash = 0
        encode = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        for ch in s[:9]:
            hash = (hash << 2) + encode[ch]

        mask = (1 << 20) - 1
        res = set()
        records = set()
        for i, ch in enumerate(s[9:]):
            hash = (hash << 2) | encode[ch]
            hash &= mask
            if hash in records:
                res.add(s[i : i + 10])
            else:
                records.add(hash)

            # print(s[i : i + 10], "{0:b}".format(hash).zfill(20))

        return list(res)