#!/opt/anaconda3/bin/python
# -*- coding: utf-8 -*-

# This bot tweets 7 jeopardy questions at 7pm each night.
# Questions taken from https://www.reddit.com/r/datasets/comments/1uyd0t/200000_jeopardy_questions_in_a_json_file/

# Housekeeping: do not edit
import tweepy, time, random, json
from credentials import *
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# What the bot will tweet
filename = open('/Users/tculler/Desktop/bot-tutorial-jumpstart/JEOPARDY_QUESTIONS1.json') 
data = json.load(filename)

real_tweet_text = []

for item in data:
    real_tweet_text.append('Category: ' + item['category'] + '; ' + item['question'][1:-1])

print(real_tweet_text[0])

# over the course of one minute, tweet jeopardy questions, waiting 8 seconds between each
timespan = time.time() + 60 * 1

while time.time() < timespan:    
    # print(random.choice(real_tweet_text))
    api.update_status(status=random.choice(real_tweet_text))
    time.sleep(8) 

# print("All done!")

# To quit early: CTRL+C and wait a few seconds
