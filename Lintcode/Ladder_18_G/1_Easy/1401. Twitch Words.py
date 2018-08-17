class Solution:
    """
    @param str: the origin string
    @return: the start and end of every twitch words
    """
    def twitchWords(self, str):
        results = []
        i = 0
        n = len(str)
        while i < n - 2:
            if str[i] == str[i + 1] and str[i] == str[i + 2]:
                start = i
                end = i + 2
                while end + 1 < n and str[end] == str[end + 1]:
                    end += 1
                
                results.append([start, end])
                
                i = end
            
            i += 1
            
        return results