class Solution:
    """
    @param arrs: the arrays
    @return: the number of the intersection of the arrays
    """
    def intersectionOfArrays(self, arrs):
        numShouldBe = len(arrs) - 1
        remains = {}

        for n in arrs[0]:
            remains[n] = numShouldBe

        ans = 0
        for i in range(1, len(arrs)):
            for n in arrs[i]:
                if n not in remains:
                    continue

                remains[n] -= 1
                if remains[n] == 0:
                    del remains[n]
                    ans += 1

                if len(remains) == 0:
                    return ans

        return ans