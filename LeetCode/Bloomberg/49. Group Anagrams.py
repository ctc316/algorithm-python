class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anas = {}
        for s in strs:
            key = str(sorted(s))
            if key not in anas:
                anas[key] = []
            anas[key].append(s)

        return anas.values()