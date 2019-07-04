class Solution:
    """
    @param n: a positive integer
    @param primes: the given prime list
    @return: the nth super ugly number
    """
    def nthSuperUglyNumber(self, n, primes):
        from queue import PriorityQueue
        pq = PriorityQueue()
        pq.put(1)
        visited = set()
        visited.add(1)

        for _ in range(n - 1):
            num = pq.get()
            for p in primes:
                new_num = num * p
                if new_num in visited:
                    continue
                pq.put(new_num)
                visited.add(new_num)

        return pq.get()