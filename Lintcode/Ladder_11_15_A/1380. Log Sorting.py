class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """
    def compare(self, x, y):
        sep_x = x.find(" ")
        id_x = x[:sep_x]
        content_x = x[sep_x + 1:]
        isalpha_x = content_x[0].isalpha()

        sep_y = y.find(" ")
        id_y = y[:sep_y]
        content_y = y[sep_y + 1:]
        isalpha_y = content_y[0].isalpha()

        if not isalpha_x and not isalpha_y:
            return 1

        if not isalpha_y:
            return -1

        if not isalpha_x:
            return 1

        if content_x != content_y:
            if content_x < content_y:
                return -1
            else:
                return 1

        if id_x < id_y:
            return -1
        else:
            return 1


    def logSort(self, logs):
        from functools import cmp_to_key
        return sorted(logs, key=cmp_to_key(self.compare))