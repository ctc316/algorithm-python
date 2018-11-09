class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        freq = {}
        for ch in s:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch] += 1

        freq_list = sorted([(v, k) for k, v in freq.items()])
        freq_list.reverse()

        result = ""
        for f in freq_list:
            for _ in range(f[0]):
                result += f[1]

        return result
