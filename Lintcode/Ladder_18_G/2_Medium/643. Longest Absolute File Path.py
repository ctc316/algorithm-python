class Solution:
    """
    @param input: an abstract file system
    @return: return the length of the longest absolute path to file
    """
    def lengthLongestPath(self, input):
        longest = 0
        record = [0 for _ in range(len(input) + 1)]
        for line in input.split("\n"):
            level = line.rfind("\t") + 1
            leng = len(line) - level
            if "." in line:
                longest = max(longest, record[level - 1] + leng)
            else:
                record[level] = record[level - 1] + leng + 1 # +1 for "\"

        return longest