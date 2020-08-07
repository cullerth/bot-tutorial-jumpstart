#!/opt/anaconda3/bin/python
# -*- coding: utf-8 -*-

# This bot tweets 7 random jeopardy questions at 7pm each night.
# Questions taken from https://www.reddit.com/r/datasets/comments/1uyd0t/200000_jeopardy_questions_in_a_json_file/

# follow at https://twitter.com/BotJumpstart

# Housekeeping: do not edit
import tweepy, time, random, json
from credentials import *
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

# What the bot will tweet
filename = open('/Users/tculler/Desktop/bot-tutorial-jumpstart/JEOPARDY_QUESTIONS1.json') 
data = json.load(filename)

categories = []
values = []
questions = []
answers = []
air_dates = []

for item in data:
    categories.append(item['category'])
    values.append(item['value'])
    questions.append(item['question'][1:-1])
    answers.append(item['answer'])
    air_dates.append(item['air_date'])

tweet_tuples = list(zip(categories,values,questions,answers,air_dates))

# over the course of one minute, tweet jeopardy questions, waiting 8 seconds between each
timespan = time.time() + 60 * 1

while time.time() < timespan:
    try:     
        tweet = random.choice(tweet_tuples)
        question = tweet[0] + " for " + tweet[1] + "; " + tweet[2]
        answer = "ANSWER: \n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n.\n \n" + tweet[3] + "; \n\noriginally aired on " + tweet[4]

        print('\n*******************\n')
        print(question)
        print(answer)

        thread_start = api.update_status(status=question)
        api.update_status(status=answer, in_reply_to_status_id=thread_start.id)

        time.sleep(8)
    except: 
        error_message = "Oop! Looks like Watson encountered an error. We're in real jeopardy now. *heavily distorted final jeopardy music begins playing over the loudspeaker...in the distance: sirens*"
        print(error_message)
        # api.update_status(status=error_message)

print("\nAll done!")

# To quit early: CTRL+C and wait a few seconds
