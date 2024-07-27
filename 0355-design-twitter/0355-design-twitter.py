class User:
    def __init__(self, userId):
        self.userId = userId

        # List of user's tweets as tuples (timestamp, tweetId)
        self.tweets = []

        # Set makes sense for these since you can't follow someone twice
        self.followers = set()
        self.follows = set()


class Twitter:
    def __init__(self):
        self.users = {}

        # Time of the world for Tweet ordering
        self.globalTime = 0

    def createUserIfNew(self, userId):
        # Only create the user if they haven't been created yet
        if userId not in self.users:
            self.users[userId] = User(userId)

    def postTweet(self, userId: int, tweetId: int) -> None:
        # Create user who is posting
        self.createUserIfNew(userId)

        # Add Tweet as tuple (timestamp, tweetId)
        # This way they can be ordered by timestamp in the news feed
        self.users[userId].tweets.append((self.globalTime, tweetId))

        # Tick time forward by 1 'tweet'
        self.globalTime += 1
    
    def getNewsFeed(self, userId):
        # Create the user if new
        self.createUserIfNew(userId)

        # Create an aggregated list of all tweets
        # Start with this user's tweets
        aggregated_tweets = list(self.users[userId].tweets)

        # Extend the list with all of the users they are following's tweets
        for followee in self.users[userId].follows:
            aggregated_tweets.extend(followee.tweets)
        
        # Sort the aggregated tweets by timestamp in descending order
        aggregated_tweets.sort(key = lambda x: x[0], reverse=True)
        
        # Extract the top 10 tweetIds
        feed = [tweet[1] for tweet in aggregated_tweets[:10]]
        return feed
        

    def follow(self, followerId: int, followeeId: int) -> None:
        # Create the users if new
        self.createUserIfNew(followerId)
        self.createUserIfNew(followeeId)

        # Add the following edge
        self.users[followerId].follows.add(self.users[followeeId])

        # Add the follower edge
        self.users[followeeId].followers.add(self.users[followerId])


    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Create the users if new
        self.createUserIfNew(followerId)
        self.createUserIfNew(followeeId)

        # Unfollow only if actually a follower currently
        if self.users[followerId] in self.users[followeeId].followers:
            
            # Remove the follower edge
            self.users[followeeId].followers.remove(self.users[followerId])

            # Remove the following edge
            self.users[followerId].follows.remove(self.users[followeeId])


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
