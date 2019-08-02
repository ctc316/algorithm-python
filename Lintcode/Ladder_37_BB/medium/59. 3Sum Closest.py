class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @param target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        n = len(numbers)
        if n < 3:
            return

        numbers.sort()
        closest = 0
        distance = float("inf")
        for i in range(n - 2):
            remain = target - numbers[i]
            left = i + 1
            right = n - 1
            while left < right:
                dist = remain - numbers[left] - numbers[right]
                if abs(dist) < distance:
                    distance = abs(dist)
                    closest = numbers[i] + numbers[left] + numbers[right]

                if dist > 0:
                    left += 1
                else:
                    right -= 1

        return closest