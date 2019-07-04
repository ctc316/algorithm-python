"""
class Comparator:
    def cmp(self, a, b)
You can use Compare.cmp(a, b) to compare nuts "a" and bolts "b",
if "a" is bigger than "b", it will return 1, else if they are equal,
it will return 0, else if "a" is smaller than "b", it will return -1.
When "a" is not a nut or "b" is not a bolt, it will return 2, which is not valid.
"""


class Solution:
    # @param nuts: a list of integers
    # @param bolts: a list of integers
    # @param compare: a instance of Comparator
    # @return: nothing
    def sortNutsAndBolts(self, nuts, bolts, compare):
        '''
        ["ab","bc","dd","gg"]
        ["AB","GG","DD","BC"]
          GG   AB   BC   DD
        '''
        self.quickSort(nuts, bolts, compare.cmp, 0, len(nuts) - 1)


    def quickSort(self, nuts, bolts, cmp, start, end):
        if start >= end:
            return

        idx = self.helper(bolts, nuts[start], cmp, start, end, False)
        self.helper(nuts, bolts[idx], cmp, start, end, True)
        self.quickSort(nuts, bolts, cmp, start, idx - 1)
        self.quickSort(nuts, bolts, cmp, idx + 1, end)


    def helper(self, tosort, pivot, cmp, start, end, isNuts):
        l = start
        r = end
        for i in range(l, r + 1):
            if isNuts and cmp(tosort[i], pivot) == 0 or \
               not isNuts and cmp(pivot, tosort[i]) == 0:
                tosort[i], tosort[l] = tosort[l], tosort[i]
                l += 1
                break

        while l <= r:
            while l <= r and (isNuts and cmp(tosort[l], pivot) == -1 or \
                          not isNuts and cmp(pivot, tosort[l]) == 1):
                l += 1

            while l <= r and (isNuts and cmp(tosort[r], pivot) == 1 or \
                          not isNuts and cmp(pivot, tosort[r]) == -1):
                r -= 1

            if l <= r:
                tosort[l], tosort[r] = tosort[r], tosort[l]
                l += 1
                r -= 1

        tosort[start], tosort[r] = tosort[r], tosort[start]
        return r