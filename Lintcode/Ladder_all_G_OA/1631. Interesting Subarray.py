class Solution:
    """
    @param a: the array a
    @return: return the maximum length
    """
    def maxLen(self, a):
        '''
          [3,2,3,1,5,2,5,1]
         0 1 2 3 4 5 6 7 8
         0 1 2 3 4 5 6 7

         0 1
         0 1

        '''
        n = len(a)
        if n <= 2:
            return n

        long_sub_start_idx = [0 for i in range(n)]
        long_sub_other_idx = [0 for i in range(n)]
        long_sub_start_idx[1] = 0
        long_sub_other_idx[1] = 0

        longest = 0
        for i in range(2, n):
            if a[i] == a[i - 1]:
                long_sub_start_idx[i] = long_sub_start_idx[i - 1]
                long_sub_other_idx[i] = long_sub_other_idx[i - 1]
            elif a[i] == a[long_sub_other_idx[i - 1]]:
                long_sub_start_idx[i] = long_sub_start_idx[i - 1]
                long_sub_other_idx[i] = i - 1
            else:
                long_sub_start_idx[i] = long_sub_other_idx[i - 1] + 1
                long_sub_other_idx[i] = i - 1

            longest = max(longest, i - long_sub_start_idx[i] + 1)

        return longest