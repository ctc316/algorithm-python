# Version 1: Naive, Time: O(n ^ 2 * max_word_len), TLE
class Solution:
    """
    @param words: a string array
    @return: the maximum product
    """
    def maxProduct(self, words):
        n = len(words)
        if n < 2:
            return 0

        maxi = 0
        for i in range(n):
            for j in range(i + 1, n):
                if self.isShareLetters(words[i], words[j]):
                    continue

                maxi = max(maxi, len(words[i]) * len(words[j]))

        return maxi


    def isShareLetters(self, word1, word2):
        letters = [False for _ in range(26)]
        for w in word1:
            letters[ord(w) - 97] = True

        for w in word2:
            if letters[ord(w) - 97]:
                return True

        return False


# Version 2: Bit manipulation, Time O(n ^ 2)
class Solution:
    """
    @param words: a string array
    @return: the maximum product
    """
    def maxProduct(self, words):
        n = len(words)
        if n < 2:
            return 0
            
        # use 26(32) bits to store the existing letters
        letter_bits = [0 for _ in range(n)]
        for i in range(n):
            bits = 0
            for ch in words[i]:
                bits |= 1 << ord(ch) - 97
            
            letter_bits[i] = bits
            
        maxi = 0
        for i in range(n):
            for j in range(i + 1, n):
                if letter_bits[i] & letter_bits[j] == 0:
                    maxi = max(maxi, len(words[i]) * len(words[j]))
        
        return maxi