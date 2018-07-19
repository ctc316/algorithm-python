# Version 1: Naive count prime
class Solution:
    """
    @param L: an integer
    @param R: an integer
    @return: the count of numbers in the range [L, R] having a prime number of set bits in their binary representation
    """
    def countPrimeSetBits(self, L, R):
        '''
            10 ~ 15
          1010   1111
           C(3,2) - 1 + C(3, 3)

            6   0110
        6 - 1   0101
        6&(6-1) 0100
        '''
        import math

        count = 0
        for i in range(L, R + 1):
            ones = 0
            while i > 0:
                ones += 1
                i &= i - 1

            if ones < 2:
                continue

            isPrime = True
            for j in range(2, int(math.sqrt(ones)) + 1):
                if ones % j == 0:
                    isPrime = False

            if isPrime:
                count += 1

        return count


# Version 2: 厄拉多塞篩法
import math
    
class Solution:
    """
    @param L: an integer
    @param R: an integer
    @return: the count of numbers in the range [L, R] having a prime number of set bits in their binary representation
    """
    def countPrimeSetBits(self, L, R):
        '''
            6     0110   
        6 - 1     0101
        6 & (6-1) 0100   remove the least significant 1
        '''
        
        count = 0
        isDeleted = [False for _ in range(L, R + 1)]
        for i in range(L, R + 1):
            if isDeleted[i - L]:
                continue
            
            if self.isWithPrimeOnes(i):
                count += 1
                while i <= R:
                    isDeleted[i - L]
                    i <<= 1
          
        return count
    
    
    def isWithPrimeOnes(self, num):
        ones = 0
        while num > 0:
            ones += 1
            num &= num - 1
            
        if ones < 2:
            return False
            
        isPrime = True
        for j in range(2, int(math.sqrt(ones)) + 1):
            if ones % j == 0:
                isPrime = False
                
        return isPrime