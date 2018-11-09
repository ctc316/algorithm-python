class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        left = 0
        right = len(heights) - 1
        left_max = 0
        right_max = 0
        result = 0
        while left <= right:
            if left_max < right_max:
                cur_height = heights[left]
                left_max = max(left_max, heights[left])
                left += 1
            else:
                cur_height = heights[right]
                right_max = max(right_max, heights[right])
                right -= 1

            if cur_height < left_max and cur_height < right_max:
                result += min(left_max, right_max) - cur_height

        return result