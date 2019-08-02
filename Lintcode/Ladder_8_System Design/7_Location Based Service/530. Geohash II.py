class GeoHash:
    """
    @param: geohash: geohash a base32 string
    @return: latitude and longitude a location coordinate pair
    """
    def decode(self, geohash):
        BASE32 = "0123456789bcdefghjkmnpqrstuvwxyz"
        bits = ""
        for ch in geohash:
            bits += self.index2bits(BASE32.find(ch))

        odd_bits = ''.join([bits[i] for i in range(0, len(bits), 2)])
        even_bits = ''.join([bits[i] for i in range(1, len(bits), 2)])

        return (self.convert2loc(-90.0, 90.0, even_bits), self.convert2loc(-180.0, 180.0, odd_bits))


    def index2bits(self, idx):
        bits = ""
        for i in range(5):
            if idx % 2 == 0:
                bits = '1' + bits
            else:
                bits = '0' + bits
            idx //= 2

        return bits


    def convert2loc(self, start, end, string):
        for ch in string:
            mid = start + (end - start) / 2.0
            if ch == '0':
                start = mid
            else:
                end = mid

        return start + (end - start) / 2.0
