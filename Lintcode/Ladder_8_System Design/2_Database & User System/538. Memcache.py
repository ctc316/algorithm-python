class Memcache:
    def __init__(self):
        self.cache = {}  # val, expire_at

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: An integer
    """
    def get(self, curtTime, key):
        if key not in self.cache:
            return 2147483647

        rec = self.cache[key]
        if rec[1] != 0 and curtTime >= rec[1]:
            # self.delete(curtTime, key)
            return 2147483647

        return rec[0]


    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: value: An integer
    @param: ttl: An integer
    @return: nothing
    """
    def set(self, curtTime, key, value, ttl):
        self.cache[key] = (value, 0 if ttl == 0 else curtTime + ttl)


    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: nothing
    """
    def delete(self, curtTime, key):
        if key in self.cache:
            del self.cache[key]


    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def incr(self, curtTime, key, delta):
        val = self.get(curtTime, key)
        if val == 2147483647:
            return val

        newVal = self.cache[key][0] + delta
        self.cache[key] = (newVal, self.cache[key][1])
        return newVal


    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def decr(self, curtTime, key, delta):
        return self.incr(curtTime, key, -delta)