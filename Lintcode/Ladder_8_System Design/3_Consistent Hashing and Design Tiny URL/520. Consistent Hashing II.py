class Solution:
    """
    @param {int} n a positive integer
    @param {int} k a positive integer
    @return {Solution} a Solution object
    """
    @classmethod
    def create(cls, n, k):
        solution = cls()
        solution.ids = set()
        solution.machines = {}
        solution.n = n
        solution.k = k
        return solution

    """
    @param: machine_id: An integer
    @return: a list of shard ids
    """
    def addMachine(self, machine_id):
        import random
        ids = []
        for _ in range(self.k):
            id = random.randint(0, self.n - 1)
            while id in self.ids:
                id = random.randint(0, self.n - 1)

            ids.append(id)
            self.ids.add(id)

        self.machines[machine_id] = sorted(ids)
        return self.machines[machine_id]

    """
    @param: hashcode: An integer
    @return: A machine id
    """
    def getMachineIdByHashCode(self, hashcode):
        machine_id = -1
        distance = self.n + 1
        for m_id, shards in self.machines.items():
            import bisect
            shard_idx = bisect.bisect_left(shards, hashcode) % len(shards)
            d = shards[shard_idx] - hashcode
            if d < 0:
                d += self.n
            if d < distance:
                distance = d
                machine_id = m_id

        return machine_id