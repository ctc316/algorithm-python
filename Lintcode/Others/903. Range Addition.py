# time: O(len of updates) + O(length)
class Solution:
    """
    @param length: the length of the array
    @param updates: update operations
    @return: the modified array after all k operations were executed
    """
    def getModifiedArray(self, length, updates):
        if length == 0:
            return []

        update_res = [0 for _ in range(length + 1)]
        for u in updates:
            update_res[u[0]] += u[2]
            update_res[u[1] + 1] -= u[2]

        result = [0 for _ in range(length)]
        result[0] = update_res[0]
        for i in range(1, length):
            result[i] = result[i - 1] + update_res[i]

        return result