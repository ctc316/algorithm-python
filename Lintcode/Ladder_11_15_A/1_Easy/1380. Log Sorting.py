class Solution:
    """
    @param logs: the logs
    @return: the log after sorting
    """
    def logSort(self, logs):

        def cmp_to_key(mycmp):
            'Convert a cmp= function into a key= function'
            class K:
                def __init__(self, obj, *args):
                    self.obj = obj
                def __lt__(self, other):
                    return mycmp(self.obj, other.obj) < 0
                def __gt__(self, other):
                    return mycmp(self.obj, other.obj) > 0
                def __eq__(self, other):
                    return mycmp(self.obj, other.obj) == 0
                def __le__(self, other):
                    return mycmp(self.obj, other.obj) <= 0
                def __ge__(self, other):
                    return mycmp(self.obj, other.obj) >= 0
                def __ne__(self, other):
                    return mycmp(self.obj, other.obj) != 0
            return K

        def compare(x, y):
            x_ = x.split(" ")
            y_ = y.split(" ")
            if len(x_) == len(y_):
                for i in range(len(x_)):
                    if x_[i] == y_[i]:
                        continue
                    if x_[i] < y_[i]:
                        return -1
                    else:
                        return 1

            return len(x_) - len(y_)


        logs.sort(key=cmp_to_key(compare))
        return logs