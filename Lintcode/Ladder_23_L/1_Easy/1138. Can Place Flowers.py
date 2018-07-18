class Solution:
    """
    @param flowerbed: an array
    @param n: an Integer
    @return: if n new flowers can be planted in it without violating the no-adjacent-flowers rule
    """
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True

        size = len(flowerbed)
        for i in range(size):
            if flowerbed[i] == 1 or  \
               i > 0 and flowerbed[i - 1] == 1 or \
               i < size - 1 and flowerbed[i + 1] == 1:
                continue

            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True

        return False