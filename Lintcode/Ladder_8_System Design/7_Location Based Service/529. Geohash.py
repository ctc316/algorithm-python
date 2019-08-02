class GeoHash:
    """
    @param: latitude: one of a location coordinate pair
    @param: longitude: one of a location coordinate pair
    @param: precision: an integer between 1 to 12
    @return: a base32 string
    """
    def encode(self, latitude, longitude, precision):
        bits_num = precision * 3
        lat_bits = self.getBits(latitude, -90, 90, bits_num)
        lng_bits = self.getBits(longitude, -180, 180, bits_num)

        bits = ''
        for i in range(bits_num):
            bits += lng_bits[i] + lat_bits[i]

        hash_code = ''
        BASE32 = "0123456789bcdefghjkmnpqrstuvwxyz"
        for i in range(0, bits_num * 2, 5):
            hash_code += BASE32[int(bits[i:i + 5], 2)]

        return hash_code[:precision]


    def getBits(self, value, left, right, bits_num):
        bits = ''
        for i in range(bits_num):
            mid = left + (right - left) / 2.0
            if value > mid:
                left = mid
                bits += '1'
            else:
                right = mid
                bits += '0'
        return bits