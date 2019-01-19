class Solution:
    """
    @param startString:
    @param endString:
    @return: Return true or false
    """
    def canTransfer(self, startString, endString):
        '''
        1. Different length;
        2. If any character is more than 2, this character cannot map to multiple character; (i.e. 'aa'-->'bc' false;)
        3. StartString is a permutation of endString (except for StartString == EndString)
        '''

        if len(startString) != len(endString):
            return False

        start_last_end = {}
        start_count = [0 for _ in range(26)]
        end_count = [0 for _ in range(26)]
        for i in range(len(startString)):
            s = startString[i]
            e = endString[i]
            s_idx = ord(s) - ord('a')
            e_idx = ord(e) - ord('a')

            if start_count[s_idx] > 0 and start_last_end.get(s, "") != e:
                return False

            start_count[s_idx] += 1
            end_count[e_idx] += 1
            start_last_end[s] = e

        # check permutation
        for i in range(26):
            if start_count[i] != end_count[i]:
                return True

        return False