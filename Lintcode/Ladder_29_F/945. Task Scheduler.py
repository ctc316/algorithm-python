class Solution:
    """
    @param tasks: the given char array representing tasks CPU need to do
    @param n: the non-negative cooling interval
    @return: the least number of intervals the CPU will take to finish all the given tasks
    """
    def leastInterval(self, tasks, n):
        '''
        n = 2
        AAAABBBCCD

        |A B C G|A B C|A B D|A E F|
        '''

        counts = [0 for _ in range(26)]
        for t in tasks:
            counts[ord(t) - 65] += 1

        counts.sort()

        i = 25
        while i >= 0 and counts[i] == counts[25]:
            i -= 1

        # counts[25] -> max
        # n + 1 -> cycle_len
        # 25 - i -> letters having the max size
        return max(len(tasks), (counts[25] - 1) * (n + 1) + 25 - i)