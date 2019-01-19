class Solution:
    """
    @param fa: the father
    @param val: the val
    @return: the biggest node
    """
    def treeProblem(self, fa, val):
        n = len(val)
        num_nodes = [1 for _ in range(n)]
        sums = [val[i] for i in range(n)]
        maxi_avg = -sys.maxsize - 1
        maxi_node = -1
        for i in range(n - 1, -1, -1):
            avg = sums[i] / num_nodes[i]
            if avg >= maxi_avg:
                maxi_avg = avg
                maxi_node = i

            if i == 0:
                break

            fa_idx = fa[i] - 1
            num_nodes[fa_idx] += num_nodes[i]
            sums[fa_idx] += sums[i]

        return maxi_node + 1