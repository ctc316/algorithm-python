class Solution:
    """
    @param target: the target
    @param array: an array
    @return: the closest value
    """
    def closestTargetValue(self, target, array):
        array.sort()

        left = 0
        right = len(array) - 1
        closest = -sys.maxsize - 1

        while left < right:
            sum = array[left] + array[right]
            if closest < sum and sum <= target:
                closest = sum

            if sum < target:
                left += 1
            else:
                right -= 1

        if closest == -sys.maxsize - 1:
            return -1

        return closest