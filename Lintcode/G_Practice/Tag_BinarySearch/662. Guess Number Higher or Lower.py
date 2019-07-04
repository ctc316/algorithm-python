"""
The guess API is already defined for you.
@param num, your guess
@return -1 if my number is lower, 1 if my number is higher, otherwise return 0
you can call Guess.guess(num)
"""


class Solution:
    # @param {int} n an integer
    # @return {int} the number you guess
    def guessNumber(self, n):
        start = 1
        end = n
        while start + 1 < end:
            mid = start + (end - start) // 2
            g = Guess.guess(mid)
            if g == 0:
                return mid
            elif g == -1:
                end = mid
            else:
                start = mid

        if Guess.guess(start) == 0:
            return start
        return end