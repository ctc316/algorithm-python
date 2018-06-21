class Solution:
    """
    @param A: a string
    @param B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):
        if len(A) != len(B):
            return False

        count = {}
        for s in A:
            if s in count:
                count[s] += 1
            else:
                count[s] = 1

        for s in B:
            if s in count and count[s] > 0:
                count[s] -= 1
            else:
                return False

        return True