class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """
    def findMissingRanges(self, nums, lower, upper):
        res = []
        cur = lower
        i = 0
        n = len(nums)
        while i < n:
            while i < n and cur >= nums[i]:
                cur = nums[i] + 1
                i += 1

            if i == n:
                break

            diff = nums[i] - cur
            if diff == 0:
                pass
            elif diff == 1:
                res.append(str(cur))
            else:
                res.append("{}->{}".format(cur, nums[i] - 1))

            cur = nums[i] + 1
            i += 1

        if upper == cur:
            res.append(str(cur))
        elif upper - cur >= 1:
            res.append("{}->{}".format(cur, upper))

        return res