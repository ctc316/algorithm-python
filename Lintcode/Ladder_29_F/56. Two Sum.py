class Solution:
    """
    @param numbers: An array of Integer
    @param target: target = numbers[index1] + numbers[index2]
    @return: [index1, index2] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        idxMap = {}
        for i, v in enumerate(numbers):
            remain = target - v
            if remain in idxMap:
                return [idxMap[remain], i]

            idxMap[v] = i

        return []