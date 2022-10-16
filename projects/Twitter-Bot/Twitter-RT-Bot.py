import tweepy
import time

print("Testing The bot")  # Test

api_key = "enter you token here"
api_secret = "enter you token here"
bearer_token = r"enter you token here"

access_token = "enter you token here"
access_token_secret = "enter you token here"

client = tweepy.Client(
    bearer_token, api_key, api_secret, access_token, access_token_secret
)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)

api = tweepy.API(auth)


class MyStream(tweepy.StreamingClient):
    def on_tweet(self, tweet):  # detects the tweet
        print(tweet.text)
        time.sleep(0.3)  # to slow up the coming tweets a bit
        try:
            client.retweet(tweet.id)
        except Exception as error:
            print(error)


stream = MyStream(bearer_token=bearer_token)

rule = tweepy.StreamRule(
    "(#Python OR #python OR #programming OR #coding) (-is:retweet -is:reply)"
)  # setting rule on what topics you want to Retweet and not to add replies and retweets. This will only pickup the original tweets, you may wish to add functionalities according to your requirements

stream.add_rules(rule)
stream.filter()
print("Your bot is now live!!")
