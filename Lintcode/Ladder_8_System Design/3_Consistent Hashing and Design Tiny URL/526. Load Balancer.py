class LoadBalancer:
    def __init__(self):
        self.servers = {}

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        self.servers[server_id] = 1

    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        if server_id in self.servers:
            del self.servers[server_id]

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        from random import choice
        return choice(list(self.servers.keys()))