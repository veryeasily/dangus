import config

import os
from pprint import pp

from praw import Reddit

USERNAME = os.environ.get("REDDIT_USERNAME")
PASSWORD = os.environ.get("REDDIT_PASSWORD")
CLIENT_ID = os.environ.get("REDDIT_CLIENT_ID")
SECRET_TOKEN = os.environ.get("REDDIT_SECRET_TOKEN")

# ensure we have the environment variables set
if not USERNAME or not PASSWORD or not CLIENT_ID or not SECRET_TOKEN:
    print(
        "You need to set the environment variables REDDIT_USERNAME, REDDIT_PASSWORD, REDDIT_CLIENT_ID, and REDDIT_SECRET_TOKEN"
    )
    exit(1)

reddit = Reddit(
    client_id=CLIENT_ID,
    client_secret=SECRET_TOKEN,
    username=USERNAME,
    password=PASSWORD,
    user_agent="DangusBot/0.0.1",
)

print("Testing auth with reddit:")
pp(reddit.user.me())

subreddit = reddit.subreddit("pythonforengineers")

last_sub = None

for submission in subreddit.hot(limit=5):
    last_sub = submission
    pp(submission.title)

pp(last_sub)
