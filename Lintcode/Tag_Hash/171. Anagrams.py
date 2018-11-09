class Solution:
    """
    @param strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        records = {} # code, list
        results = []
        for s in strs:
            code = self.encode(s)
            if code not in records:
                records[code] = []

            records[code].append(s)

        for val in records.values():
            if len(val) > 1:
                results.extend(val)

        return results


    def encode(self, string):
        counts = [0 for _ in range(26)]
        for ch in string:
            counts[ord(ch) - 97] += 1

        code = ""
        for i in range(len(counts)):
            if counts[i] > 0:
                code += str(i) + str(counts[i]) + "_"

        return code