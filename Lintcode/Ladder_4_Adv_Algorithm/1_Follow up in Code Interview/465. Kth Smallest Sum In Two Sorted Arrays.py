class Solution:
    """
    @param A: an integer arrays sorted in ascending order
    @param B: an integer arrays sorted in ascending order
    @param k: An integer
    @return: An integer
    """
    def kthSmallestSum(self, A, B, k):
        num_A = len(A)
        num_B = len(B)
        if num_A == 0 or num_B == 0:
            return 0

        from queue import PriorityQueue
        pq = PriorityQueue()
        pq.put((A[0] + B[0], 0, 0)) # val, a_idx, b_idx
        visited = set()
        visited.add(0)

        count = 0
        while not pq.empty():
            val, a_idx, b_idx = pq.get()
            count += 1
            if count == k:
                return val

            next_a = a_idx + 1
            key_a = next_a * num_B + b_idx
            if next_a < num_A and key_a not in visited:
                visited.add(key_a)
                pq.put((A[next_a] + B[b_idx], next_a, b_idx))

            next_b = b_idx + 1
            key_b = a_idx * num_B + next_b
            if next_b < num_B and key_b not in visited:
                visited.add(key_b)
                pq.put((A[a_idx] + B[next_b], a_idx, next_b))

        return -1