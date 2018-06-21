class Solution:
    """
    @param head: the given linked list
    @return: the array that store the values in reverse order
    """
    def reverseStore(self, head):
       results = []
       while head:
           results.append(head.val)
           head = head.next

       return results[::-1]