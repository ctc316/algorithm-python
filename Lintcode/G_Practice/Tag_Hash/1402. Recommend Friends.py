class Solution:
    """
    @param friends: people's friends
    @param user: the user's id
    @return: the person who most likely to know
    """
    def recommendFriends(self, friends, user):
        n = len(friends)
        friends_set = [set(f) for f in friends]
        most_common = 0
        most_common_user = -1
        for other in [i for i in range(n) if i != user and i not in friends_set[user]]:
            common = len(friends_set[user]) - len(friends_set[user] - friends_set[other])
            if common > most_common:
                most_common = common
                most_common_user = other

        return most_common_user