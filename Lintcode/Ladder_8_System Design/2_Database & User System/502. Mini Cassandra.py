"""
Definition of Column:
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value
"""


class MiniCassandra:

    def __init__(self):
        self.db = {}

    """
    @param: row_key: a string
    @param: column_key: An integer
    @param: value: a string
    @return: nothing
    """
    def insert(self, row_key, column_key, column_value):
        if row_key not in self.db:
            self.db[row_key] = {}

        self.db[row_key][column_key] = column_value


    """
    @param: row_key: a string
    @param: column_start: An integer
    @param: column_end: An integer
    @return: a list of Columns
    """
    def query(self, row_key, column_start, column_end):
        ret = []
        if row_key not in self.db:
            return ret

        for k, v in sorted(self.db[row_key].items(), key=lambda (k, v): k):
            if k >= column_start and k <= column_end:
                ret.append(Column(k, v))

        return ret