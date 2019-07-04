class Solution:
    """
    @param nums: a list of integers
    @return: return a boolean
    """
    def isPossible(self, nums):
        counts = {}
        tails = {}
        for num in nums:
            counts[num] = counts[num] + 1 if num in counts else 1

        for num in nums:
            if counts[num] == 0:
                continue
            counts[num] -= 1
            if num - 1 in tails and tails[num - 1] > 0:
                tails[num - 1] -= 1
                tails[num] = tails[num] + 1 if num in tails else 1
            elif num + 1 in counts and counts[num + 1] > 0 and \
                 num + 2 in counts and counts[num + 2] > 0:
                     tails[num + 2] = tails[num + 2] + 1 if num + 2 in tails else 1
                     counts[num + 1] -= 1
                     counts[num + 2] -= 1
            else:
                return False

        return True