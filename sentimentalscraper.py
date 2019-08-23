#!/usr/bin/python
# -*- coding: utf-8 -*-

import tweepy
import csv
import json
import numpy as np
import matplotlib.pyplot as plt

positive_sentiment = 0
negative_sentiment = 0


with open('positive-words.txt') as posi:
        positive_words = set(posi.read().split())

with open('negative-words.txt') as nega:
        negative_words = set(nega.read().split())


# Twitter API credentials
consumer_key = 'BSgxwTIxLls8VYCORWCQZ31Te'
consumer_secret = 'CrD6rwrMpZkAgaiO2vKBUbb0zZOZvcn7VoEwLwoocJWQCj7zzk'

# api endpoint
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
api = tweepy.API(auth)

# Mention the maximum number of tweets that you want to be extracted.

num_tweets = int(input('Enter the number of tweets you want to analyze: '))
if num_tweets > 1000:
	num_tweets = 1000


topic = input('Enter the topic you want to scrape: ')

for tweet in tweepy.Cursor(api.search, q= topic,
rpp=100).items(num_tweets):

	sentiments = list(str(tweet.text.encode('utf-8')).split())
	for i in sentiments:
		if i.lower() in positive_words:
			positive_sentiment += 1

		if i.lower() in negative_words:
			negative_sentiment += 1

positive_percent = round(positive_sentiment*100/(positive_sentiment+negative_sentiment), 2)
negative_percent = round(negative_sentiment*100/(positive_sentiment+negative_sentiment), 2)

print(topic+" recieves "+str(positive_percent)+"% positive sentiment and "+str(negative_percent)+"% negative sentiment")
print(str(positive_sentiment+negative_sentiment)+" of the last "+str(num_tweets)+" tweets expressed sentiment.")


objects = ('Positive Sentiment', 'Negative Sentiment')
y_pos = np.arange(len(objects))
performance = [positive_percent, negative_percent]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('Sentiment')
plt.title('Share of Positive and Negative sentiment')

plt.show()
















