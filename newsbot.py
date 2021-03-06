#!/usr/bin/env python3
import praw
import tldextract
from colorama import Fore, Back, Style
import secrets


def niceprint_hot_submissions(N, names):
	reddit = praw.Reddit(client_id=secrets.client_id, client_secret=secrets.client_secret, password=secrets.password, user_agent=secrets.user_agent, username=secrets.username)
	print(Back.BLACK)
	for name in names:
		subreddit = reddit.subreddit(name)
		hot = subreddit.hot(limit=N+4) #couple extra if some stickied posts
		print(Style.RESET_ALL + Back.BLACK + '\n' + Style.BRIGHT + 'reddit.com/r/' + name + '\n')
		n=0
		for submission in hot:
			if submission.stickied or n>=N:
				continue

			n+=1 
			print(Style.DIM + '{}. '.format(n) + Style.NORMAL + '{}'.format(submission.title))
			print(Style.DIM + '(source: {}, score: {})\n'.format(tldextract.extract(submission.url).registered_domain, submission.ups))

	print(Style.RESET_ALL)

subreddits = ['worldnews','news']
niceprint_hot_submissions(5, subreddits)