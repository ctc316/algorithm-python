class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def minArea(self, image, x, y):
        if image is None or len(image) == 0:
            return 0

        if image[0] is None or len(image[0]) == 0:
            return 0

        n = len(image)
        m = len(image[0])

        # x lower bound
        start = 0
        end = x
        x_low = -1
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if self.checkBlack(image, range(mid, mid + 1), range(m)):
                end = mid
            else:
                start = mid

        if self.checkBlack(image, range(start, start + 1), range(m)):
            x_low = start
        else:
            x_low = end

        # x higher bound
        start = x
        end = n - 1
        x_high = -1
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if self.checkBlack(image, range(mid, mid + 1), range(m)):
                start = mid
            else:
                end = mid

        if self.checkBlack(image, range(end, end + 1), range(m)):
            x_high = end
        else:
            x_high = start

        # y lower bound
        start = 0
        end = y
        y_low = -1
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if self.checkBlack(image, range(n), range(mid, mid + 1)):
                end = mid
            else:
                start = mid

        if self.checkBlack(image, range(n), range(start, start + 1)):
            y_low = start
        else:
            y_low = end

        # y higher bound
        start = y
        end = m - 1
        y_high = -1
        while start + 1 < end:
            mid = int(start + (end - start) / 2)
            if self.checkBlack(image, range(n), range(mid, mid + 1)):
                start = mid
            else:
                end = mid

        if self.checkBlack(image, range(n), range(end, end + 1)):
            y_high = end
        else:
            y_high = start


        return (x_high - x_low + 1) * (y_high - y_low + 1)



    def checkBlack(self, image, xrange, yrange):
        for x in xrange:
            for y in yrange:
                if image[x][y] == "1":
                    return True

        return Falses