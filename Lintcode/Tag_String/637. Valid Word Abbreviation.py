class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def validWordAbbreviation(self, word, abbr):
        n = len(word)
        m = len(abbr)
        i = 0
        j = 0
        while i < n and j < m:
            num = 0
            while j < m and abbr[j].isdigit():
                num = num * 10 + int(abbr[j])
                if num == 0:
                    break
                j += 1
            
            if num != 0:
                i += num
                continue
            
            if word[i] != abbr[j]:
                return False
            
            i += 1
            j += 1
        
        return i == n and j == m