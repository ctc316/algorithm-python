class Solution:
    """
    @param s: the given string
    @return: all the palindromic permutations (without duplicates) of it
    """
    def generatePalindromes(self, s):
        counts = {}
        for ch in s:
            if ch not in counts:
                counts[ch] = 1
            else:
                counts[ch] += 1

        odd = ""
        for k, v in counts.items():
            if v % 2 == 1:
                if odd:
                    return []
                odd = k
            counts[k] //= 2

        options = []
        for k, v in counts.items():
            for _ in range(v):
                options.append(k)

        results = []
        self.dfs(options, "", results)
        return [r + odd + r[::-1] for r in results]


    def dfs(self, options, combi, results):
        if not options:
            results.append(combi)

        for i in range(len(options)):
            if i > 0 and options[i] == options[i - 1]:
                continue

            combi += options[i]
            removed = options.pop(i)
            self.dfs(options, combi, results)
            combi = combi[:-1]
            options.insert(i, removed)