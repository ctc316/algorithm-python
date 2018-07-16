class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        if len(numbers) < 4:
           return []

        numbers.sort()

        n = len(numbers)
        results = []

        for i in range(n - 3):
            if i != 0 and numbers[i] == numbers[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j != i + 1 and numbers[j] == numbers[j - 1]:
                    continue

                base = numbers[i] + numbers[j]
                start = j + 1
                end = n - 1
                while start < end:
                    sum = base + numbers[start] + numbers[end]
                    if sum > target:
                        end -= 1
                    elif sum < target:
                        start += 1
                    else:
                        results.append([numbers[i], numbers[j], numbers[start], numbers[end]])
                        start += 1
                        end -= 1
                        while start < end and numbers[start] == numbers[start - 1]:
                            start += 1
                        while start < end and numbers[end] == numbers[end + 1]:
                            end -= 1

        return results