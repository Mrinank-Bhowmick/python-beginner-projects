import tweepy
import time

print("Testing The bot")  # Test

api_key = "enter your API key here"
api_secret = "enter your API secret key here"
access_token = "enter your access token here"
access_token_secret = "enter your access token secret here"

# You should create an OAuthHandler, not a Client
auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_token, access_token_secret)

# Initialize the Twitter API
api = tweepy.API(auth)


class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        # Check if the tweet is not a retweet and not a reply
        if not status.retweeted and status.in_reply_to_status_id is None:
            print(status.text)
            try:
                api.retweet(status.id)
                print("Retweeted")
            except tweepy.TweepError as e:
                print(e.reason)

    def on_error(self, status_code):
        if status_code == 420:
            print("Error 420: Enhance Your Calm - Rate Limited")
            return False


# Create a stream listener
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

# Specify the keywords and filter criteria
keywords = ["#Python", "#python", "#programming", "#coding"]
myStream.filter(track=keywords, languages=["en"])
