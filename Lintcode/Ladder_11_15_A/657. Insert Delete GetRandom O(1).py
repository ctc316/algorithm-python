class RandomizedSet:

    def __init__(self):
        self.store = set()

    """
    @param: val: a value to the set
    @return: true if the set did not already contain the specified element or false
    """
    def insert(self, val):
        if val in self.store:
            return False
        self.store.add(val)
        return True

    """
    @param: val: a value from the set
    @return: true if the set contained the specified element or false
    """
    def remove(self, val):
        if val not in self.store:
            return False
        self.store.remove(val)
        return True

    """
    @return: Get a random element from the set
    """
    def getRandom(self):
        import random
        return random.choice(list(self.store))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param = obj.insert(val)
# param = obj.remove(val)
# param = obj.getRandom()