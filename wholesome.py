"""Prints out Random Wholesome Post Using Praw - Used locally"""
import os
from typing import Generator
from random import randrange
import praw
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

env = {
    'username': os.getenv("REDDITNAME"),
    'password': os.getenv("PASSWORD"),
    'id': os.getenv("APPID"),
    'secret': os.getenv("APISECRET"),
    'app-name': os.getenv("APPNAME"),
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


if __name__ == "__main__":
    submission = wholesomify(20)
    print(f"title: {submission.title} \n url: {submission.url}")
