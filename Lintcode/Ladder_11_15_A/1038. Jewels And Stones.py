class Solution:
    """
    @param J: the types of stones that are jewels
    @param S: representing the stones you have
    @return: how many of the stones you have are also jewels
    """
    def numJewelsInStones(self, J, S):
        cnt = 0
        J = set([c for c in J])
        for s in S:
            if s in J:
                cnt += 1

        return cnt