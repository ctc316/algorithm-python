class Solution:
    """
    @param A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        n = len(A)
        if n == 0:
            return 0

        # index紀錄第幾個全排列，至少為1，初始的全排列為增序
        # factor 計算 n!, 代表數字交換後有幾種變異情況
        index = 1
        factor = 1

        for i in range(n - 1, -1, -1):
            # 算該數後面有幾個比它小的數字
            count = 0
            for j in range(i + 1, n):
                if A[j] < A[i]:
                    count += 1

            index += factor * count
            factor *= n - i

        return index