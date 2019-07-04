class Solution:
    """
    @param s:
    @param str:
    @return: Output whether this combination meets the condition
    """
    def checkWord(self, s, str):
        dict = set(str)
        stack = []
        visited = set()

        if s not in dict:
            return False

        stack.append(s)
        visited.add(s)
        while stack:
            word = stack.pop()
            if len(word) == 1:
                return True

            for i in range(len(word)):
                next = word[:i] + word[i + 1:]
                if next not in dict or next in visited:
                    continue

                visited.add(next)
                stack.append(next)

        return False
