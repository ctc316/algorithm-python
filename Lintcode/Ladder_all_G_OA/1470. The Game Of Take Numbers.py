class Solution:
    """
    @param arr: the array
    @return: the winner
    """
    def theGameOfTakeNumbers(self, arr):
        odd = 0
        even = 0
        for i in range(len(arr)):
            if i % 2 == 1:
                odd += arr[i]
            else:
                even += arr[i]

        if even >= odd:
            return 1

        return 1 if (len(arr) - 1) % 2 else 2

        

class Solution:
    """
    @param arr: the array
    @return: the winner
    """
    def theGameOfTakeNumbers(self, arr):
        n = len(arr)
        if n == 0:
            return 1

        summ = [0 for _ in range(n)]
        for leng in range(1, n + 1):
            for i in range(n - leng + 1):
                if leng == 1:
                    summ[i] = arr[i];
                    continue;

                summ[i] = max(arr[i + leng - 1] - summ[i], arr[i] - summ[i + 1])

        return 1 if summ[0] >= 0 else 2