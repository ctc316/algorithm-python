class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        n = len(source)
        m = len(target)
        if n == 0 or m == 0:
            return ""

        ch_needs = {}
        for ch in target:
            if ch not in ch_needs:
                ch_needs[ch] = 1
            else:
                ch_needs[ch] += 1

        done_cnt = 0
        done_need = len(ch_needs)

        minimum = float('Inf')
        min_window = (0, 0)
        
        last_start = n - m
        start = 0
        end = 0
        while start <= last_start:
            if done_cnt == done_need:
                ch = source[start]
                if ch in ch_needs:
                    ch_needs[ch] += 1
                    if ch_needs[ch] == 1:
                        done_cnt -= 1

                start += 1

            elif end == n:
                break

            else:
                ch = source[end]
                if ch in ch_needs:
                    ch_needs[ch] -= 1
                    if ch_needs[ch] == 0:
                        done_cnt += 1
                end += 1

            if done_cnt == done_need:
                if end - start < minimum:
                    minimum = end - start
                    min_window = (start, end)


        return source[min_window[0]:min_window[1]]