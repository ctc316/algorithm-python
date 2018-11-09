# Version 1
class Solution:
    """
    @param startString:
    @param endString:
    @return: Return true or false
    """
    def canTransfer(self, startString, endString):
        '''
            abbcd   -->  effgg
            12234        12233

         X  abacd   -->  effgg
            12134        12233

         X  abbcd   -->  efgfg
            12234        12323
        '''
        if len(startString) != len(endString):
            return False

        rec = {}
        count = 0
        code = []
        for i in range(len(endString)):
            if endString[i] not in rec:
                count += 1
                rec[endString[i]] = count

            code.append(rec[endString[i]])

        rec = {}
        count = 0
        for i in range(len(startString)):
            if startString[i] not in rec:
                count += 1
                rec[startString[i]] = count

            if rec[startString[i]] < code[i]:
                return False

        return True


# Version 2: TLE
class Solution:
    """
    @param startString:
    @param endString:
    @return: Return true or false
    """
    def canTransfer(self, startString, endString):
        from queue import Queue
        q = Queue()
        visited = set()

        q.put(startString)
        visited.add(startString)

        while not q.empty():
            s = q.get()
            for next_str in self.getTransforms(s):
                if next_str in visited:
                    continue

                if next_str == endString:
                    return True

                q.put(next_str)
                visited.add(next_str)

        return False


    def getTransforms(self, string):
        results = []
        for src in [chr(97 + i) for i in range(26)]:
            for tar in [chr(97 + i) for i in range(26)]:
                if src == tar:
                    continue

                new_str = string.replace(src, tar)
                if new_str != string:
                    results.append(new_str)

        return results


