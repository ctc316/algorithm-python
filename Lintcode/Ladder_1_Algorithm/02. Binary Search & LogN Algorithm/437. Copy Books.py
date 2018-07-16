# Version 1: Binary Search, Time: O(nlogm)
class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        if len(pages) == 0:
            return 0

        # max = pages[0]
        # sum = 0
        # for i in range(len(pages)):
        #     sum += pages[i]
        #     if max < pages[i]:
        #         max = pages[i]
        # start = max
        # end = sum

        start = 0
        end = 1e12
        while start + 1 < end:
            print(start, end)
            mid = int(start + (end - start) / 2)
            if self.isValid(pages, mid, k):
                end = mid
            else:
                start = mid

        if self.isValid(pages, start, k):
            return start

        return end


    def isValid(self, pages, bound, k):
        copiers = 0
        remain = 0
        for p in pages:
            if p > bound:
                return False

            if p > remain:
                copiers += 1
                remain = bound

            remain -= p

        return copiers <= k