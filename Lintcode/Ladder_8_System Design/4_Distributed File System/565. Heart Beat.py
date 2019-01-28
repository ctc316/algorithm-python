class HeartBeat:

    def __init__(self):
        # do intialization if necessary
        pass

    """
    @param: slaves_ip_list: a list of slaves'ip addresses
    @param: k: An integer
    @return: nothing
    """
    def initialize(self, slaves_ip_list, k):
        self.heartbeats = {}
        self.k = k
        for s in slaves_ip_list:
            self.heartbeats[s] = 0


    """
    @param: timestamp: current timestamp in seconds
    @param: slave_ip: the ip address of the slave server
    @return: nothing
    """
    def ping(self, timestamp, slave_ip):
        if slave_ip not in self.heartbeats:
            return

        self.heartbeats[slave_ip] = timestamp

    """
    @param: timestamp: current timestamp in seconds
    @return: a list of slaves'ip addresses that died
    """
    def getDiedSlaves(self, timestamp):
        ret = []
        for slave, tms in self.heartbeats.items():
            if timestamp - tms >= 2 * self.k:
                ret.append(slave)

        return ret