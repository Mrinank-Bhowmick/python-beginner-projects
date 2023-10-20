## TWITTER-BOT

This basic python project involves creating a Twitter bot using Tweepy to retweet tweets that contain certain hashtags related to Python and programming. 
Well, before that you might need to install:
```bash
pip install tweepy
```
This file includes the detailed and concise explanation of the project code as follows:

1. Created a "MyStreamListener" class that inherits from "tweepy.StreamListener". This class defines how the bot should behave when it receives tweets.

2. In the "on_status" method of "MyStreamListener", it checks if the tweet is not a retweet and not a reply before retweeting. This ensures that you only retweet original tweets and not replies or retweets.

3. In the "on_error" method of "MyStreamListener", it handles error code 420 (rate limit exceeded) by printing a message and returning False to stop the stream.

4. Used the "myStream.filter" method to filter tweets with the specified keywords and language ("en" for English).

5. Make sure to replace "enter your API key here", "enter your API secret key here", "enter your access token here", and "enter your access token secret here" with your actual Twitter API credentials.

## Note: Remember that running a Twitter bot should comply with Twitter's terms of service and automation rules. Be cautious not to exceed rate limits or engage in spammy behavior.


