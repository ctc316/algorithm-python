class Solution:
    """
    @param sentence: a list of string
    @param rows: an integer
    @param cols: an integer
    @return: return an integer, denote times the given sentence can be fitted on the screen
    """
    def wordsTyping(self, sentence, rows, cols):
        cnts = [len(word) for word in sentence]
        if max(cnts) > cols:
            return 0
        
        n = len(cnts)
        times = 0
        row = 0
        col = 0
        i = 0 
        while row < rows:
            if cnts[i] <= cols - col:
                col += cnts[i] + 1
                i += 1
                if i == n:
                    i = 0
                    times += 1
            else:
                row += 1
                col = 0
                if times > 0 and i == 0:
                    return times * rows // row
                
        return times
