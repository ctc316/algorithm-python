class Solution:
    """
    @param height: the given height
    @param width: the given width
    @return: the number of paths you can reach the end
    """
    def uniquePath(self, height, width):
        rolling_len = 2
        path_counts = [[0 for _ in range(height)] for __ in range(rolling_len)]
        path_counts[0][0] = 1
        cur = 0
        prev = 0
        cur_height = 1
        for i in range(1, width):
            cur = i % rolling_len
            if cur_height < height:
                cur_height += 1
                
            for j in range(cur_height):
                path_counts[cur][j] = path_counts[prev][j]
                if j > 0:
                    path_counts[cur][j] += path_counts[prev][j - 1]
                if j < height - 1:
                    path_counts[cur][j] += path_counts[prev][j + 1]

                path_counts[cur][j] %= 1000000007

            prev = cur

        return path_counts[(width - 1) % rolling_len][0]