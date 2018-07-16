"""
class FlipTool:

    @classmethod
    def flip(cls, arr, i):
        ...
"""
class Solution:
    """
    @param array: an integer array
    @return: nothing
    """
    def pancakeSort(self, array):
        """
            [6, 4, 5, 2, 1, 3]
            1st           target

            sorting from the last position,
            in each round, try reverse the max value to the 1st,
            then move the 1st to target position by reversing
        """

        for target in range(len(array) - 1, 0, -1):
            for i in range(target, 0, -1):
                if array[i] > array[0]:
                    FlipTool.flip(array, i)

            FlipTool.flip(array, target)