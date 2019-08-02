class Solution:
    """
    @param n: the number
    @return: the rank of the number
    """
    def kthPrime(self, n):
        primes = []
        for num in range(2, n + 1):
            is_prime = True
            bound = num ** 0.5
            for p in primes:
                if p > bound:
                    break
                if num % p == 0:
                    is_prime = False
                    break

            if is_prime:
                primes.append(num)

        return len(primes)
