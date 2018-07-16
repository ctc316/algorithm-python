class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        if len(S) < 3:
           return 0

        S.sort()

        count = 0
        for target in range(2, len(S)):
            start = 0
            end = target - 1
            while start < end:
                if S[start] + S[end] > S[target]:
                    count += end - start
                    end -= 1
                else:
                    start += 1

        return count