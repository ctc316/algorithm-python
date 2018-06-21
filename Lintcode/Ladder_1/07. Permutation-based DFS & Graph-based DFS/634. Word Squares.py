# Version 1: DFS, Time Limit Exceeded 
class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """
    def wordSquares(self, words):
        if len(words) == 0 or len(words[0]) == 0:
            return []

        results = []
        self.dfs(words, len(words[0]), [], results)
        return results


    def dfs(self, words, n, wordsqr, results):
        if len(wordsqr) == n:
            results.append(wordsqr[:])
            return

        row = len(wordsqr)
        for newWord in words:
            matched = True
            for i in range(row):
                if newWord[i] != wordsqr[i][row]:
                    matched = False
                    break

            if matched:
                wordsqr.append(newWord)
                self.dfs(words, n, wordsqr, results)
                wordsqr.pop()



# Version2: Tires + DFS
class Trie:
    def __init__(self, words):
        self.trie = {}
        if len(words) > 0:
            for word in words:
                self.add(word, 0)
    
    def add(self, word, start):
        t = self.trie
        for i in range(start, len(word)):
            if word[i] not in t:
                t[word[i]] = {}
            t = t[word[i]]
       
    def get(self, prefix):
        # skip prefix
        t = self.trie
        for ch in prefix:
            if ch not in t:
                return []
            t = t[ch]
            
        # collect all words with this prefix
        results = []
        self.collect(t, prefix, results)
        return results
        
    def collect(self, t, prefix, results):
        if not t:
            if len(prefix) > 0:
                results.append(prefix)
            return
            
        for ch in t:
            self.collect(t[ch], prefix + ch, results)
       

class Solution:
    """
    @param: words: a set of words without duplicates
    @return: all word squares
    """
    def wordSquares(self, words):
        if len(words) == 0 or len(words[0]) == 0:
            return []
        
        trie = Trie(words)
        results = []
        self.dfs(words, trie, len(words[0]), '', [], results)
        return results
        

    def dfs(self, word, trie, n, prefix, wordsqr, results):
        candidates = trie.get(prefix)
        rows = len(wordsqr) + 1
        for cand in candidates:
            wordsqr.append(cand)
            if rows == n:
                results.append(wordsqr[:])
            else:
                nextPrefix = ""
                for i in range(rows):
                    nextPrefix += wordsqr[i][rows]
                self.dfs(word, trie, n, nextPrefix, wordsqr, results)
            wordsqr.pop()