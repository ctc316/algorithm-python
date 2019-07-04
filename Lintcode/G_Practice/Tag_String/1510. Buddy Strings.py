class Solution:
    """
    @param A: string A
    @param B: string B
    @return: bool
    """
    def buddyStrings(self, A, B):
        if len(A) != len(B) or len(A) < 2 or sorted(list(A)) != sorted(list(B)):
            return False

        if A == B:
            chars = set()
            for a in A:
                if a in chars:
                    return True
                else:
                    chars.add(a)
            return False

        n = len(A)
        diff_idx = []
        for i in range(n):
            if A[i] != B[i]:
                diff_idx.append(i)

        return len(diff_idx) == 2 and A[diff_idx[0]] == B[diff_idx[1]] and A[diff_idx[1]] == B[diff_idx[0]]




class Solution:
    """
    @param A: string A
    @param B: string B
    @return: bool
    """
    def buddyStrings(self, A, B):
        # Write your code here
        if len(A) != len(B):
            return False
        if A == B and len(set(A)) < len(A):
            return True
        dif = [(a, b) for a, b in zip(A, B) if a != b]
        return len(dif) == 2 and dif[0] == dif[1][::-1]