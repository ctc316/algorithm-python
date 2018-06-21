import random

class Solution:
    """
    @param {int} n a positive integer
    @param {int} k a positive integer
    @return {Solution} a Solution object
    """
    @classmethod
    def create(cls, n, k):
        sol = cls()
        sol.hashmap = {}
        sol.n = n
        sol.k = k
        return sol

    """
    @param: machine_id: An integer
    @return: a list of shard ids
    """
    def addMachine(self, machine_id):
        ret = []
        for i in range(self.k):
            code = random.randint(0, self.n - 1)
            while code in self.hashmap:
                code = random.randint(0, self.n - 1)

            self.hashmap[code] = machine_id
            ret.append(code)

        ret.sort()
        return ret

    """
    @param: hashcode: An integer
    @return: A machine id
    """
    def getMachineIdByHashCode(self, hashcode):
        for i in range(self.n):
            hashcode %= self.n
            if hashcode in self.hashmap:
                return self.hashmap[hashcode]
            hashcode += 1