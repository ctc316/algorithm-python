class Solution:
    """
    @param height: the given height
    @param width: the given width
    @return: the number of paths you can reach the end
    """
    def uniquePath(self, height, width):
        counts = [0 for _ in range(height)]
        counts[0] = 1
        for i in range(1, width):
            nextCnts = [0 for _ in range(height)]
            for j in range(height):
                if counts[j] > 0:
                    nextCnts[j] += counts[j]
                    if j - 1 >= 0:
                        nextCnts[j - 1] += counts[j]
                    if j + 1 < height:
                        nextCnts[j + 1] += counts[j]

            counts = nextCnts

        return counts[0] % 1000000007