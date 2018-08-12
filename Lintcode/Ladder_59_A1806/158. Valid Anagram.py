class Solution:
    """
    @param s: The first string
    @param t: The second string
    @return: true or false
    """
    def anagram(self, s, t):
        counts = {}
        for ch in s:
            if ch in counts:
                counts[ch] += 1
            else:
                counts[ch] = 1

        for ch in t:
            if ch not in counts:
                return False

            counts[ch] -= 1
            if counts[ch] == 0:
                del counts[ch]

        return len(counts.keys()) == 0