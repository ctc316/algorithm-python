'''
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''

class MiniTwitter:

    def __init__(self):
        # do intialization if necessary
        self.user_timeline = {}
        self.user_follows = {}

    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """
    def postTweet(self, user_id, tweet_text):
        tweet = Tweet(user_id, tweet_text)

        if user_id not in self.user_timeline:
            self.user_timeline[user_id] = []
        self.user_timeline[user_id].insert(0, tweet)

        if len(self.user_timeline[user_id]) > 10:
            self.user_timeline[user_id].pop()

        return tweet

    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """
    def getNewsFeed(self, user_id):
        newsfeed = []
        follows = [user_id]
        if user_id in self.user_follows:
            follows.extend(list(self.user_follows[user_id]))
        for f in follows:
            if f not in self.user_timeline:
                continue

            newsfeed.extend(self.user_timeline[f])
            newsfeed.sort(key=lambda x: x.id, reverse=True)
            newsfeed = newsfeed[:10]

        return newsfeed


    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """
    def getTimeline(self, user_id):
        if user_id not in self.user_timeline:
            return []
        return self.user_timeline[user_id]


    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def follow(self, from_user_id, to_user_id):
        if from_user_id not in self.user_follows:
            self.user_follows[from_user_id] = set()
        self.user_follows[from_user_id].add(to_user_id)


    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """
    def unfollow(self, from_user_id, to_user_id):
        if from_user_id in self.user_follows:
            self.user_follows[from_user_id].remove(to_user_id)