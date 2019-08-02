class Solution:
    """
    @param pid: the process id
    @param ppid: the parent process id
    @param kill: a PID you want to kill
    @return: a list of PIDs of processes that will be killed in the end
    """
    def killProcess(self, pid, ppid, kill):
        childs = {p:[] for p in pid}
        for i, pp in enumerate(ppid):
            if pp in childs:
                childs[pp].append(pid[i])

        result = []
        from queue import Queue
        q = Queue()
        q.put(kill)

        while not q.empty():
            id = q.get()
            result.append(id)
            for child in childs[id]:
                if child in childs:
                    q.put(child)

        return result