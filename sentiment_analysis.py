import tweepy
from textblob import TextBlob

consumer_key='13WuI1J9RCEqGN2rb7DIaxPFw'
consumer_secret='5LaMMskcnmLXi55VVDjpgoJxVRRZw8WA0T6qj6aWmT6HcBiVZ7'
access_token='28784535-KZuyD5S8uDF7yzP79ePuK2yejzhG4kKV8jJ1iSrWv'
access_token_secret='XtnjQWYGAX3o4xek8YKTNXwrAs6SSwd5niWXvsY59hrqS'
auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
public_tweets= api.search('Trump')
for tweet in public_tweets:
    print(tweet.text)
    analysis=TextBlob(tweet.text)
    print(analysis.sentiment)
