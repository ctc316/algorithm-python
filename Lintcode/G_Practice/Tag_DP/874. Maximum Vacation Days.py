class Solution:
    """
    @param flights: the airline status from the city i to the city j
    @param days: days[i][j] represents the maximum days you could take vacation in the city i in the week j
    @return: the maximum vacation days you could take during K weeks
    """
    def maxVacationDays(self, flights, days):
        changes = collections.defaultdict(list)
        cities, weeks = len(days), len(days[0])
        for i in range(cities):
            for j in range(cities):
                if flights[i][j] or i == j:
                    changes[j].append(i)

        prev = [0] + [float('-inf')] * (cities - 1)
        cur = prev[:]

        for week in range(weeks):
            for city in range(cities):
                cur[city] = max(prev[i] for i in changes[city]) + days[city][week]
            prev = cur[:]
        return max(cur)
