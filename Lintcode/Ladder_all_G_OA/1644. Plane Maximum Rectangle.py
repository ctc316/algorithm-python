class Solution:
    """
    @param a: the points
    @return: return the maximum rectangle area
    """
    def getMaximum(self, a):
        points = set([(x[0], x[1]) for x in a])
        a.sort()
        max_area = 0
        for i in range(len(a)):
            for j in range(i + 1, len(a)):
                if a[j][0] <= a[i][0] or a[j][1] <= a[i][1]:
                    continue

                if (a[i][0], a[j][1]) not in points or (a[j][0], a[i][1]) not in points:
                    continue

                max_area = max(max_area, (a[j][0] - a[i][0]) * (a[j][1] - a[i][1]))

        return max_area