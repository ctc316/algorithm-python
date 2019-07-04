class Solution:
    """
    @param A: lists A
    @param B: lists B
    @return: the index mapping
    """
    def anagramMappings(self, A, B):
        pos_map = {v: i for i, v in enumerate(B)}
        return [pos_map[v] for v in A]