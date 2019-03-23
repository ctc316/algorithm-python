class Solution:
    """
    @param t: the length of the flight
    @param dur: the length of movies
    @return: output the lengths of two movies
    """
    def aerial_Movie(self, t, dur):
        t -= 30
        dur.sort()
        left = 0
        right = len(dur) - 1
        longest = 0
        longest_pair = None
        while left < right:
            summ = dur[left] + dur[right]
            if summ <= t:
                if summ > longest:
                    longest = summ
                    longest_pair = [dur[left], dur[right]]
                left += 1
            else:
                right -= 1

        return longest_pair
