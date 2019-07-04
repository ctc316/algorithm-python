class Solution:
    """
    @param a: the list of salary
    @param target: the target of the sum
    @return: the cap it should be
    """
    def getCap(self, a, target):
        start = min(a)
        end = target // len(a) + 1
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





class Solution:
    """
    @param a: the list of salary
    @param target: the target of the sum
    @return: the cap it should be
    """
    def getCap(self, a, target):
        a.sort()
        summ = 0
        for i in range(len(a) - 1, -1, -1):
            ex = (target - summ) // (i + 1)
            print(summ, ex, a[i])
            if ex >= a[i]: 
                return ex + 1 if (target - summ) % (i + 1) else ex
            summ += a[i]
        return -1