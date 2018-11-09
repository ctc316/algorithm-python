class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        count = {}
        for ch in s:
            if ch not in count:
                count[ch] = 1
            else:
                count[ch] += 1

        has_odd = False
        for v in count.values():
            if v % 2 == 1:
                if has_odd:
                    return False

                has_odd = True

        return True