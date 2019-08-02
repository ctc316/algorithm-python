class Solution:
    def __init__(self):
        self.cache = {}
        self.reject_cache = set()

    """
    @param: timestamp: the current timestamp
    @param: event: the string to distinct different event
    @param: rate: the format is [integer]/[s/m/h/d]
    @param: increment: whether we should increase the counter
    @return: true or false to indicate the event is limited or not
    """
    def isRatelimited(self, timestamp, event, rate, increment):
        req_key = "{}_{}_{}".format(timestamp, event, rate)
        if req_key in self.reject_cache:
            return True

        limit, dur_type = rate.split("/")
        limit = int(limit)

        if dur_type == 'd':
            cur = timestamp // 3600
            duration = 24
            keyFunc = self.getCacheKeyHour
        elif dur_type == 'h':
            cur = timestamp // 60
            duration = 60
            keyFunc = self.getCacheKeyMin
        else:
            cur = timestamp
            duration = 1 if dur_type == 's' else 60
            keyFunc = self.getCacheKeySec

        count = 0
        for tms in range(cur, max(-1, cur - duration), -1):
            count += self.cache.get(keyFunc(tms, event), 0)

        if count >= limit:
            self.reject_cache.add(req_key)
            return True

        if increment:
            for func in [self.getCacheKeySec, self.getCacheKeyMin, self.getCacheKeyHour]:
                key = func(timestamp, event)
                if key in self.cache:
                    self.cache[key] += 1
                else:
                    self.cache[key] = 1

        return False


    def getCacheKeySec(self, timestamp, event):
        return event + "_s_" + str(timestamp)

    def getCacheKeyMin(self, timestamp, event):
        return event + "_m_" + str(timestamp // 60)

    def getCacheKeyHour(self, timestamp, event):
        return event + "_h_" + str(timestamp // 3600)