class Solution:
    """
    @param s: the IP string
    @return: All possible valid IP addresses
    """
    def restoreIpAddresses(self, s):
        n = len(s)

        if n < 4:
            return []

        results = []
        for i in range(1, n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    sectors = [s[0:i], s[i:j], s[j:k], s[k:n]]
                    isValid = True
                    for sec in sectors:
                        if len(sec) > 3 or int(sec) > 255 or \
                            len(sec) > 1 and sec[0] == '0':
                            isValid = False
                            break

                    if isValid:
                        results.append(".".join(sectors))

        return results