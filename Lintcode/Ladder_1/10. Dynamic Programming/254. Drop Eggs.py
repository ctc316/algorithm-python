class Solution:
    """
    @param n: An integer
    @return: The sum of a and b
    """
    def dropEggs(self, n):
        '''
        我们需要让每多扔一次鸡蛋1，鸡蛋2的线性搜索最坏情况减少1，
        这样恩能够保持整体最坏情况的平衡
        假设鸡蛋1第一次在第X层扔，然后向上X-1层扔一次，然后向上X-2层扔，
        以此类推直到100层，那么我们通过下面的公式求出X：
        X + (X-1) + (X-2) + ... + 1 = 100 -> X = 14

        找平衡（等差數列）
        X  +  (X-1)         +    (X-2)        + ... + 1 = 100 -> X = 14
        蛋1丟14 + 蛋2丟13(+蛋1丟1=14) + 12(+蛋1丟2=14)
        14F  27F     39F
        '''

        # X(X + 1)/2 = 100 -> 求X
        res = 1
        sum = 1
        while sum < n:
            res += 1
            sum += res
        return res


# Version 2: 公式解
class Solution:
    """
    @param n: An integer
    @return: The sum of a and b
    """
    def dropEggs(self, n):
        return math.ceil((math.sqrt(8 * n) - 1) / 2)