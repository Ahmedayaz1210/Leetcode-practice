'''
UNDERSTAND:
- Inputs: Given a Twitter class and we need to design some functions
    - Need to initialize our class
    - Post a tweet with a new tweetId by the userId, pretty much incrementing tweetId
    - getNewsFeed which gets last 10 most recent tweets from the userId or any other user(s) they follow, so getting last 10 tweets in decreasing order by tweetId number
    - follow which takes a followerId and follows the followeeId
    - unfollow which is the vice versa of above function
- Need to design all these functions
- TC? SC?
- 1 <= userId, followerId, followeeId <= 500
- 0 <= tweetId <= 10^4
- Do tweets have unique ID? Yes
- At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow
- A user can't follow themselves

MATCH:
- So for tweetId and retrieving 10 most recent we can use max heap
- To check if user follows any other user(s), we can use a hashmap and create key value pairs
- To store each user's tweets and when they were posted we can use another hashmap which will store the tweetId and the timestamp of when it was posted

PLAN:
- Initializing function:
    - Create a following dictionary which can keep who follows who and keep it a set to ensure no user Id gets saved twice, cuz a user can only follow another user once
    - Create a tweets dictionary which stores all the tweets a certain userId posted with a time stamp which will help in max heap to retrieve 10 most recent ones
    - Lastly create that time stamp

- postTweet function:
    - When post tweet is called
    - Have user and tweet id
    - Appen the tweet id and time stamp as a list into the user id as a value pair in the tweet dictionary

- follow/unfollow
    - pretty easy
    - add and remove followeeId as a value for followerId in following dictionary

- getNewsFeed
    - Take the user id append it to a user set
    - Now take its following users from following dict and add to this set
    - Take all users from set, append their tweets to a max heap by negating time
    - pop out 10 most recent with only thr tweetId, return this list

EVALUATE:
- The problem isn't hard, it feels like too much information thrown at once
- Wording did make it seem harder, once you figured out data structures it gets easier
- Nevertheless I would say got 50% of the problem myself
Time Complexity:

getNewsFeed(): O(n) where n is total followees

Earlier we said O(F + UTlog(U*T)), but in the worst case:
U (users) = n (total followees + user themselves)
Since we only get 10 tweets max, the log factor becomes less significant
So simplified to O(n)


Other methods (postTweet, follow, unfollow): O(1)

These just involve simple dictionary and set operations
No iteration or complex data structure manipulation



Space Complexity: O(Nm + NM + n)
Let's understand each term:

N*m: Storage for all tweets

N users, each with up to m tweets
This is for our tweets dictionary


N*M: Storage for following relationships

N users, each following up to M other users
This is for our following dictionary


n: Additional space used in getNewsFeed

For storing users set and heap
n is number of followees for that specific user

'''
from heapq import heapify, heappush, heappop
from collections import defaultdict
class Twitter:

    def __init__(self):
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1
        self.tweets[userId].append([self.time, tweetId]) #time goes first so it's easier to put in max heap later

    def getNewsFeed(self, userId: int) -> List[int]:
        users = {userId}
        users.update(self.following[userId])

        max_heap = []
        for user in users:
            for time, tweetId in self.tweets[user]:
                heappush(max_heap, [-time, tweetId])
        res = []
        while max_heap and len(res) < 10:
            recent = heappop(max_heap)
            res.append(recent[1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)