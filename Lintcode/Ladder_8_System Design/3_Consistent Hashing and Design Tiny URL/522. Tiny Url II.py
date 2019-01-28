class TinyUrl2:
    def __init__(self):
        self.seq_id = 0
        self.rec_shortToLong = {}
        self.rec_longToShort = {}
        self.chars = "0123456789abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


    """
    @param: long_url: a long url
    @param: key: a short key
    @return: a short url starts with http://tiny.url/
    """
    def createCustom(self, long_url, key):
        short_url = "http://tiny.url/" + key
        if short_url in self.rec_shortToLong and self.rec_shortToLong[short_url] != long_url:
            return "error"

        if long_url in self.rec_longToShort and self.rec_longToShort[long_url] != short_url:
            return "error"

        self.rec_shortToLong[short_url] = long_url
        self.rec_longToShort[long_url] = short_url

        return short_url


    """
    @param: long_url: a long url
    @return: a short url starts with http://tiny.url/
    """
    def longToShort(self, long_url):
        if long_url in self.rec_longToShort:
           return self.rec_longToShort[long_url]

        short_url = ""
        while True:
            short_url = ""
            id = self.seq_id
            self.seq_id += 1
            while id > 0:
                short_url += self.chars[id % 62]
                id //= 62

            while len(short_url) < 6:
                short_url += self.chars[0]

            short_url = "http://tiny.url/" + short_url

            if short_url not in self.rec_shortToLong:
                break

        self.rec_shortToLong[short_url] = long_url
        self.rec_longToShort[long_url] = short_url

        return short_url


    """
    @param: short_url: a short url starts with http://tiny.url/
    @return: a long url
    """
    def shortToLong(self, short_url):
        if short_url in self.rec_shortToLong:
           return self.rec_shortToLong[short_url]

        return ""
