# This is a library to fetch tweets before scanning them

import requests
import tweepy

TWITTER_TOKEN = "Bearer AAAAAAAAAAAAAAAAAAAAAPkXWgEAAAAADnJAibXPBwvpl91ZmjnlkBe4foQ%3DeHQyR8RW6XnJBM0xzfldLCy8zT6YbyRPnz1RmMMgc3YCAqzCNs"
API_CONSUMER_TOKEN = "15rH8iutOInzf0FQ4Ep29kjYQ"
API_SECRET = "xvYXgEiLBa9mIDqH6HU3aVcV0yIZJCjxsvJkXUfibsA9lBEUbr"

ACCESS_TOKEN = "1467073773107134466-Bp73ktGx6xImFLY9Bulj1cCbKP0wov"
ACCESS_SECRET = "4OB13PQyDyhj3F26fHRHl6gjBoS2C9momrjLUGAWnhXyz"


BASE_URL = "https://api.twitter.com/"
DEFAULT_HEADERS = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8',
                   'Authorization': TWITTER_TOKEN}


def get_by_username(username):
    url = BASE_URL + "2/users/by/usernames=" + username
    return requests.get(url, headers=DEFAULT_HEADERS)


def get_profile_data(handle):
    url = BASE_URL + 2/users/
