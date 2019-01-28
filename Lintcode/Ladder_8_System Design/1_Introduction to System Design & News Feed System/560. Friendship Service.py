class FriendshipService:
    
    def __init__(self):
        self.followings = {}
        self.followers = {}

    """
    @param: user_id: An integer
    @return: all followers and sort by user_id
    """
    def getFollowers(self, user_id):
        if user_id not in self.followers:
            return []
        return sorted(self.followers[user_id])
        
        
    """
    @param: user_id: An integer
    @return: all followings and sort by user_id
    """
    def getFollowings(self, user_id):
        if user_id not in self.followings:
            return []
        return sorted(self.followings[user_id])


    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, to_user_id, from_user_id):
        if from_user_id not in self.followings:
            self.followings[from_user_id] = set([to_user_id])
        else:
            self.followings[from_user_id].add(to_user_id)
            
        if to_user_id not in self.followers:
            self.followers[to_user_id] = set([from_user_id])
        else:
            self.followers[to_user_id].add(from_user_id)
        

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, to_user_id, from_user_id):
        if from_user_id in self.followings and to_user_id in self.followings[from_user_id]:
            self.followings[from_user_id].remove(to_user_id)
            
        if to_user_id in self.followers and from_user_id in self.followers[to_user_id]:
            self.followers[to_user_id].remove(from_user_id)