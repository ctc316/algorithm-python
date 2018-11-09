class Solution:
    """
    @param S: a string
    @return: return a list of strings
    """
    def letterCasePermutation(self, S):
        return self.dfs(S, 0, {})

    def dfs(self, S, idx, records):
        if idx == len(S):
            return [""]

        if idx in records:
            return records[idx]

        results = []
        next_strs = self.dfs(S, idx + 1, records)
        if S[idx].isdigit():
            for s in next_strs:
                results.append(S[idx] + s)
        else:
            for s in next_strs:
                results.append(S[idx].lower() + s)
                results.append(S[idx].upper() + s)

        records[idx] = results
        return results