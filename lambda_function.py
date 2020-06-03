import json
import os
import praw
from typing import Generator
from random import randrange

env = {
    'username': os.environ["REDDITNAME"],
    'password': os.environ.get("PASSWORD",""), # for testing purposes, password is blank...
    'id': os.environ["APPID"],
    'secret': os.environ["APPSECRET"],
    'app-name': os.environ["APPNAME"],
    'limit': os.environ["LIMIT"],
}

reddit = praw.Reddit(client_id=env['id'],
                     client_secret=env['secret'],
                     user_agent=f"{env['app-name']} by {env['username']}",
                     username=env['username'],
                     password=env['password'],
                     )


def wholesomify(limit: int) -> Generator:
    # assume you have a Reddit instance bound to variable `reddit`
    choice = ["wholesomememes", "aww", "EyeBleach"]
    subreddit = reddit.subreddit(choice[randrange(len(choice))])
    submissions = []

    # populate
    for submission in subreddit.hot(limit=limit):
        submissions.append(submission)

    return submissions[randrange(limit)]


def lambda_handler(event, context):
    submission = wholesomify(int(env['limit']))
    message = f"wholesome time!: {submission.url}"

    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
