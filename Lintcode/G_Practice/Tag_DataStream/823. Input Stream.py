class Solution:
    """
    @param inputA: Input stream A
    @param inputB: Input stream B
    @return: The answer
    """
    def inputStream(self, inputA, inputB):
        resA = ""
        resB = ""
        for a in inputA:
            if a == '<':
                resA = resA[:-1]
            else:
                resA += a
                
        for b in inputB:
            if b == '<':
                resB = resB[:-1]
            else:
                resB += b
        
        return "YES" if resA == resB else "NO"
