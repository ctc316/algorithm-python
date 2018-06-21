# DP
class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        n = len(A)
        if n == 0:
            return 0

        prevMax2 = 0
        prevMax1 = A[0]

        for i in range(1, n):
            sum = max(prevMax1, prevMax2 + A[i])
            prevMax2 = prevMax1
            prevMax1 = sum

        return prevMax1