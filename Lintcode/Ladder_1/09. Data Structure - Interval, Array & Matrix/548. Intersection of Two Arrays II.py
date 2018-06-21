class Solution:

    """
    @param: nums1: an integer array
    @param: nums2: an integer array
    @return: an integer array
    """
    def intersection(self, nums1, nums2):
        if len(nums2) < len(nums1):
            temp = nums1
            nums1 = nums2
            nums2 = temp

        counts = {}
        for n in nums1:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1

        results = []
        for n in nums2:
            if n not in counts:
                continue

            counts[n] -= 1
            results.append(n)
            if counts[n] == 0:
                del counts[n]

            if len(counts) == 0:
                break

        return results