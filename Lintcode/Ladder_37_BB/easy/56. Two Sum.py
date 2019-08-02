class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        n = len(numbers)
        num_idx = sorted([(numbers[i], i) for i in range(n)])
        l = 0
        r = n - 1
        while l < r:
            remain = target - num_idx[l][0] - num_idx[r][0]
            if remain > 0:
                l += 1
            elif remain < 0:
                r -= 1
            else:
                left = num_idx[l][1]
                right = num_idx[r][1]
                return [left, right] if left < right else [right, left]