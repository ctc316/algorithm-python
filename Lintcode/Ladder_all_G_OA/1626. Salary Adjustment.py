class Solution:
    """
    @param a: the list of salary
    @param target: the target of the sum
    @return: the cap it should be
    """
    def getCap(self, a, target):
        # Write your code here.
        start = 1
        end = 10000
        while start + 1 < end:
            mid = start + (end - start) // 2
            if self.sumByCap(a, mid) < target:
                start = mid
            else:
                end = mid

        if self.sumByCap(a, start) >= target:
            return start
        return end


    def sumByCap(self, a, cap):
        res = 0
        for num in a:
            res += cap if num < cap else num

        return res