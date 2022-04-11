import re
import praw
from os import environ
import json
from datetime import datetime

env_vars = dict(environ)
bot_client_id = env_vars['REDDIT_CLIENT_ID']
bot_client_secret = env_vars['REDDIT_CLIENT_SECRET']
bot_password = env_vars['REDDIT_CLIENT_PASSWORD']
bot_name = "RickRollMatcher_Bot"

reddit = praw.Reddit(
    client_id=bot_client_id,
    client_secret=bot_client_secret,
    user_agent=bot_name,
    username=bot_name,
    password=bot_password
)

map = {"we're": 3, 'no': 1, 'strangers': 1, 'to': 4, 'love': 1, 'you': 41, 'know': 5, 'the': 3, 'rules': 1, 'and': 16, 'so': 3, 'do': 1, 'i': 3, 'a': 7, 'full': 1, "commitment's": 1, 'what': 1, "i'm": 4, 'thinking': 1, 'of': 1, "wouldn't": 1, 'get': 1, 'this': 1, 'from': 1, 'any': 1, 'other': 3, 'guy': 1, 'just': 2, 'wanna': 2, 'tell': 9, 'how': 3, 'feeling': 3, 'gotta': 2, 'make': 8, 'understand': 2, 'never': 40, 'gonna': 42, 'give': 14, 'up': 10,
       'let': 6, 'down': 6, 'run': 6, 'around': 6, 'desert': 6, 'cry': 6, 'say': 8, 'goodbye': 6, 'lie': 6, 'hurt': 6, "we've": 2, 'known': 2, 'each': 2, 'for': 2, 'long': 2, 'your': 2, "heart's": 2, 'been': 4, 'aching': 2, 'but': 2, "you're": 3, 'too': 3, 'shy': 2, 'it': 4, 'inside': 2, 'we': 4, 'both': 2, "what's": 2, 'going': 2, 'on': 2, 'game': 2, 'play': 2, 'if': 1, 'ask': 1, 'me': 2, "don't": 1, 'blind': 1, 'see': 1, 'ooh': 1, 'ooh-ooh': 3}

subreddit = reddit.subreddit("zvek")


def process_submission(submission):
    normalized_title = submission.title.lower()
    word = "title"
    if(word in normalized_title):
        submission.reply(body="This is a reply")
        print(f"Replied to {submission.author} @ {datetime.now()}")


def process_comment(comment):
    if(comment.author == bot_name):
        print("Self comment, returning...")
        return

    words = set(re.findall(r"[\w']+", comment.body))
    matchingWords = 0
    for word in words:
        if(word in map.keys()):
            matchingWords += 1
    matchPerc = round((matchingWords/len(map.keys())*100), 2)
    if(matchPerc > 10):
        comment.reply(
            f"Hey {comment.author}, your comment matches the lyrics of Never Gonna Give You Up by {matchPerc}%")
        print(f"Replied to {comment.author} @ {datetime.now()}")


def submissionHelper():
    print('Processing submissions...\n')
    for submission in subreddit.stream.submissions(skip_existing=True):
        process_submission(submission)


def commentHelper():
    print('Processing comments...\n')
    for comment in subreddit.stream.comments(skip_existing=True):
        process_comment(comment)


if(reddit.user.me() == bot_name):
    print("Success...\nRevving up inner Rick Astley\n")
    commentHelper()
