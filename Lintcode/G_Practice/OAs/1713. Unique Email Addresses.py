class Solution:
    """
    @param emails:
    @return: The number of the different email addresses
    """
    def numUniqueEmails(self, emails):
        uni_emails = set()
        for e in emails:
            local, domain = e.split("@")
            local = local.replace(".", "")
            local = local.split("+")[0]
            uni_emails.add(local + domain)

        return len(uni_emails)