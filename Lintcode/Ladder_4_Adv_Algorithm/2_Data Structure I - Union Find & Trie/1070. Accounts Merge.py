class UnionFind:
    def __init__(self):
        self.parent = {}
        self.name = {}


    def find(self, a):
        path = []
        while self.parent[a] != a:
            path.append(a)
            a = self.parent[a]

        for p in path:
            self.parent[p] = a

        return a


    def connect(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)

        if root_a != root_b:
            self.parent[root_b] = root_a


    def add(self, a, name):
        self.parent[a] = a
        self.name[a] = name


    def exist(self, a):
        return a in self.parent


class Solution:
    """
    @param accounts: List[List[str]]
    @return: return a List[List[str]]
    """
    def accountsMerge(self, accounts):
        union = UnionFind()
        for mails in accounts:
            if len(mails) < 2:
                continue

            for i in range(1, len(mails)):
                if not union.exist(mails[i]):
                    union.add(mails[i], mails[0])

            for i in range(1, len(mails) - 1):
                union.connect(mails[i], mails[i + 1])


        mail_group = {}
        for mail in union.parent.keys():
            root = union.find(mail)
            if root not in mail_group:
                mail_group[root] = set([root])

            mail_group[root].add(mail)


        results = []
        for mail, mail_list in mail_group.items():
            mail_list = list(mail_list)
            mail_list.sort()
            mail_list.insert(0, union.name[mail])
            results.append(mail_list)

        return results