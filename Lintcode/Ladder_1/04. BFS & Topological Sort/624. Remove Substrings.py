# Version 1: write own find method
class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict):

        minLen = len(s)

        from queue import Queue
        q = Queue()
        hash = set()

        q.put(s)
        hash.add(s)

        while not q.empty():
            str = q.get()
            if len(str) < minLen:
                minLen = len(str)

            self.exploreStr(q, hash, str, dict)

        return minLen


    def exploreStr(self, q, hash, str, dict):
        sLen = len(str)
        wLen = 0
        end = 0

        for word in dict:
            wLen = len(word)
            for i in range(0, sLen - wLen + 1):
                end = i + wLen
                if str[i : end] == word:
                    newStr = str[ : i] + str[end : ]
                    if newStr in hash:
                        continue
                    q.put(newStr)
                    hash.add(newStr)



# Version 2: Using string.find()
class Solution:
    """
    @param: s: a string
    @param: dict: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, dict):
        
        minLen = len(s)
        
        from queue import Queue
        q = Queue()
        hash = set()
        
        q.put(s)
        hash.add(s)
        
        while not q.empty():
            str = q.get()
            for sub in dict:
                pos = str.find(sub)
                while pos != -1:
                    newStr = str[:pos] + str[pos + len(sub):]
                    
                    if newStr not in hash:
                        if len(newStr) < minLen:
                            minLen = len(newStr)
                        q.put(newStr)
                        hash.add(newStr)

                    pos = str.find(sub, pos + 1)
    
        return minLen