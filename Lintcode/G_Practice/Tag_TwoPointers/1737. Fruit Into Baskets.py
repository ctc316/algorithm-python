class Solution:
    """
    @param tree: The type of fruit
    @return: The total amount of fruit you can collect.
    """
    def totalFruit(self, tree):
        res = cur = _1st = _2nd = basket2 = 0
        for t in tree:
            cur = cur + 1 if t in (_1st, _2nd) else basket2 + 1
            if t == _2nd:
                basket2 +=  1
            else:
                basket2 = 1
                _1st, _2nd = _2nd, t
            res = max(res, cur)
        return res