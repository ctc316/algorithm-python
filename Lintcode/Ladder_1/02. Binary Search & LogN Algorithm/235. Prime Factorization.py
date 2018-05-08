class Solution:
    """
    @param num: An integer
    @return: an integer array
    """
    def primeFactorization(self, num):
        results = []

        # 660 -> 330 -> 165 -> 55 -> 11
        i = 2
        while i * i <= num:
            while num % i == 0:
                num /= i
                results.append(i)
            i+=1

        if num != 1:
            results.append(int(num))

        return results