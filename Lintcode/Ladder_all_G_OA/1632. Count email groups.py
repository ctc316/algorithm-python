class Solution:
    """
    @param emails: Original email
    @return: Return the count of groups which has more than one email address in it.
    """
    def countGroups(self, emails):
        group_all = set()
        group_more_than_one = set()
        for email in emails:
            parts = email.split("@")
            for i in range(len(parts) - 2, -1, -1):
                parts[i] = self.removeStrAfterPlusSign(parts[i])
                parts[i] = parts[i].replace(".", "")

            result = "".join(parts)
            if result in group_all:
                group_more_than_one.add(result)
            else:
                group_all.add(result)

        return len(group_more_than_one)


    def removeStrAfterPlusSign(self, string):
        i = 0
        while i < len(string) and string[i] != '+':
            i += 1

        return string[:i]