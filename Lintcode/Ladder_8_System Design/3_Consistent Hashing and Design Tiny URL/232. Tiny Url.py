class TinyUrl:
    def __init__(self):
        self.seq_id = 0
        self.rec_shortToLong = {}
        self.rec_longToShort = {}
        self.chars = "0123456789abcedfghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    """
    @param: url: a long url
    @return: a short url starts with http://tiny.url/
    """
    def longToShort(self, url):
        if url in self.rec_longToShort:
           return self.rec_longToShort[url]

        short_url = ""
        id = self.seq_id
        self.seq_id += 1
        while id > 0:
            short_url += self.chars[id % 62]
            id //= 62

        while len(short_url) < 6:
            short_url += self.chars[0]

        short_url = "http://tiny.url/" + short_url

        self.rec_shortToLong[short_url] = url
        self.rec_longToShort[url] = short_url

        return short_url


    """
    @param: url: a short url starts with http://tiny.url/
    @return: a long url
    """
    def shortToLong(self, url):
        if url in self.rec_shortToLong:
           return self.rec_shortToLong[url]

        return ""
