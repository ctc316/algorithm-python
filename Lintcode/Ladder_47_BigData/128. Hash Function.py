class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """
    def hashCode(self, key, HASH_SIZE):
        code = 0
        for ch in key:
            code = (code * 33 + ord(ch)) % HASH_SIZE

        return code