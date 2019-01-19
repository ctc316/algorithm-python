class Solution:
    """
    @param intervalList:
    @param number:
    @return: return True or False
    """
    def isInterval(self, intervalList, number):
        for intv in intervalList:
            if intv[0] <= number and number <= intv[1]:
                return "True"

        return "False"