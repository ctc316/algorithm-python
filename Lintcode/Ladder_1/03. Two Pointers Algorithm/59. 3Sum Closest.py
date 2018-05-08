class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        if len(numbers) < 3:
            return 0

        numbers.sort()

        closest = sys.maxsize
        closestSum = 0
        for i in range(2, len(numbers)):
            start = 0
            end = i - 1
            while start < end:
                currSum = numbers[i] + numbers[start] + numbers[end]
                diff = currSum - target
                if abs(diff) < closest:
                    closest = abs(diff)
                    closestSum = currSum

                if diff > 0:
                    end -= 1
                elif diff < 0:
                    start += 1
                else:
                    return currSum

        return closestSum