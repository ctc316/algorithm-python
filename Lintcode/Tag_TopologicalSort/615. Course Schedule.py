class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        indegrees = [0] * numCourses
        edges = {}
        for p in prerequisites:
            indegrees[p[1]] += 1
            if p[0] not in edges:
                edges[p[0]] = []
            edges[p[0]].append(p[1])


        from queue import Queue
        q = Queue()

        for i, v in enumerate(indegrees):
            if v == 0:
                q.put(i)

        finished = 0
        while not q.empty():
            course = q.get()
            finished += 1
            if course in edges:
                for c in edges[course]:
                    indegrees[c] -= 1
                    if indegrees[c] == 0:
                        q.put(c)

        return finished == numCourses