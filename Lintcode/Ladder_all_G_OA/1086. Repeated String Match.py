class Solution:
    """
    @param A: a string
    @param B: a string
    @return: return an integer
    """
    def repeatedStringMatch(self, A, B):
        for i in range(len(A)):
            if A[i] == B[0]:
                result = self.search(A, B, i)
                if result > 0:
                    return result

        return -1


    def search(self, A, B, i):
        repeats = 1
        j = 0
        len_A = len(A)
        len_B = len(B)
        while i < len_A and j < len_B and A[i] == B[j]:
            i += 1
            j += 1

            if j == len_B:
                return repeats

            if i == len_A:
                repeats += 1
                i = 0

        return -1