class Solution:
    """
    @param n: the nth
    @return: the nth sequence
    """
    def countAndSay(self, n):
        # write your code here
        cur_str = '1'
        for _ in range(1, n):
            next = ''
            count = 1
            cur_ch = cur_str[0]
            for i in range(1, len(cur_str)):
                if cur_str[i] != cur_ch:
                    next += str(count) + cur_ch
                    cur_ch = cur_str[i]
                    count = 1
                else:
                    count += 1
    
            next += str(count) + cur_ch
            cur_str = next
    
        return cur_str