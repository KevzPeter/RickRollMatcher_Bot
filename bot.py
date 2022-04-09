import praw
from os import environ
import json
from datetime import datetime

env_vars = dict(os.environ)
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


def process_submission(submission):
    normalized_title = submission.title.lower()
    word = "title"
    if(word in normalized_title):
        submission.reply(body="This is a reply")
        print(f"Replied to {submission.author} @ {datetime.now()}")


def do_func():
    subreddit = reddit.subreddit("zvek")
    for submission in subreddit.stream.submissions():
        process_submission(submission)


if(reddit.user.me() == bot_name):
    do_func()
