# hashset, Time: O(n)
class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        hashs = set()
        longest = 0

        for n in num:
            hashs.add(n)

        for n in num:
            if n not in hashs:
                continue

            hashs.remove(n)

            prev = n - 1
            while prev in hashs:
                hashs.remove(prev)
                prev -= 1

            next = n + 1
            while next in hashs:
                hashs.remove(next)
                next += 1

            longest = max(longest, next - prev - 1)

        return longest