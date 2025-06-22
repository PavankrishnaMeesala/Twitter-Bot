import tweepy
from time import sleep

# Twitter API credentials
consumer_key = 'XXXX'
consumer_secret = 'XXXX'
access_token = 'XXXX'
access_token_secret = 'XXXX'
bearer_token = 'XXXX'

# OAuth 1.0a User Authentication
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# OAuth 2.0 Client for searching tweets
client = tweepy.Client(bearer_token=bearer_token)

# Twitter bot settings for liking Tweets
LIKE = False
# Retweet = True

# Twitter bot settings for following the user who tweeted
FOLLOW = False

print("Twitter bot which retweets, likes tweets and follows users")
print("Bot Settings")
print("Like Tweets :", LIKE)
print("Follow users :", FOLLOW)

# Change the hashtags to your choice
query = 'Artificial Intelligence OR AI -is:retweet lang:en'

# Search for tweets using the recent search endpoint
for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, tweet_fields=['author_id']).flatten(limit=100):
    try:
        print('\nTweet by user ID:', tweet.author_id)

        # Retweet the tweet
        api.retweet(tweet.id)
        print('Retweeted the tweet')

        # Favorite the tweet
        if LIKE:
            api.create_favorite(tweet.id)
            print('Liked the tweet')

        # Follow the user who tweeted
        if FOLLOW:
            user = api.get_user(user_id=tweet.author_id)
            if not user.following:
                api.create_friendship(user_id=tweet.author_id)
                print('Followed the user')

        # Twitter bot sleep time settings in seconds. Use large delays so that your account will not get banned
        sleep(30)

    except tweepy.TweepyException as e:
        print(e.reason)

    except StopIteration:
        break
