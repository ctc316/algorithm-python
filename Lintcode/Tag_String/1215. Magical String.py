class Solution:
    """
    @param n: an integer
    @return: the number of '1's in the first N number in the magical string S
    """
    def magicalString(self, n):
        '''
        1 22 11 2 1
        1 2  2  1 1 2
        '''
        if n == 0:
            return 0

        if n <= 3:
            return 1

        arr = [1, 2, 2]
        pos = 2
        ones = 1
        while len(arr) < n:
            amount = arr[pos]
            num = 1 if pos % 2 == 0 else 2
            if num == 1:
                ones += amount
            for _ in range(amount):
                arr.append(num)

            pos += 1

        return ones - 1 if len(arr) > n and arr[-1] == 1 else ones