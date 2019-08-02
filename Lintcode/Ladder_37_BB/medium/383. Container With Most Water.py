class Solution:
    """
    @param heights: a vector of integers
    @return: an integer
    """
    def maxArea(self, heights):
        left, right = 0, len(heights) - 1
        maxi = 0
        while left < right:
            maxi = max(maxi, min(heights[left], heights[right]) * (right - left))
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return maxi