class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        while b != 0:
            # Python 的问题： int 超過 0xFFFFFFFF 會自動轉成 long
            _a = (a ^ b) & 0xFFFFFFFF # 相加不進位
            _b = (a & b) << 1  # 同為 1 的進位
            a = _a
            b = _b

        return a