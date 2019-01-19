class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        n = len(numbers)
        if n < 3:
            return []

        numbers.sort()
        result = []
        for i in range(len(numbers)):
            if i > 0 and numbers[i] == numbers[i-1]:
                continue

            if numbers[i] > 0:
                break

            target = 0 - numbers[i]
            start = i + 1
            end = n - 1
            while start < end:
                if start > i + 1 and numbers[start] == numbers[start - 1]:
                    start += 1
                    continue

                if end < n - 1 and numbers[end] == numbers[end + 1]:
                    end -= 1
                    continue

                summ = numbers[start] + numbers[end]
                if summ == target:
                    result.append([numbers[i], numbers[start], numbers[end]])
                    start += 1
                elif summ < target:
                    start += 1
                else:
                    end -= 1

        return result