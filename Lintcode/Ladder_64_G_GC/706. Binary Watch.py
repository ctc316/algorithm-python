class Solution:
    """
    @param num: the number of "1"s on a given timetable
    @return: all possible time
    """
    def binaryTime(self, num):
        hour = [[] for _ in range(4)]
        minute = [[] for _ in range(6)];
        for i in range(0, 12):
            n = bin(i).count('1')
            hour[n].append(i)
        for i in range(0, 60):
            n = bin(i).count('1')
            minute[n].append(i)

        ans = [];
        for i in range(0, num + 1):
            if i < 4 and num - i < 6:
                for h in hour[i]:
                    for m in minute[num - i]:
                        ans.append('%d:%02d' % (h, m));
        return ans