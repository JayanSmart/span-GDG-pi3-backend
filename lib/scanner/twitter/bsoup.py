from bs4 import BeautifulSoup
import requests
import urllib.parse as tourl
import sys
import json


def search_by_displayname(displayname):
    url = "https://twitter.com/search?q=" + \
        tourl.quote_plus(displayname) + "&src=typed_query&f=user"
    response = None
    try:
        response = requests.get(url)
    except Exception as e:
        print(repr(e))
        sys.exit(1)

    if response.status_code != 200:
        print("Non success status code returned "+str(response.status_code))
        sys.exit(1)

    soup = BeautifulSoup(response.text, 'lxml')

    if soup.find("div", {"class": "errorpage-topbar"}):
        print("\n\n Error: Invalid username.")
        sys.exit(1)

    print(soup.text)
    # tweets = get_tweets_data(username, soup)

    return soup.text


def get_tweets_data(username, soup):
    tweets_list = list()
    tweets_list.extend(get_this_page_tweets(soup))


def get_this_page_tweets(soup):
    tweets_list = list()
    tweets = soup.find_all("li", {"data-item-type": "tweet"})
    for tweet in tweets:
        tweet_data = None
        try:
            # tweet_data = get_tweet_text(tweet)
            pass
        except Exception as e:
            continue
            # ignore if there is any loading or tweet error

        if tweet_data:
            tweets_list.append(tweet_data)
            print(".", end="")
            sys.stdout.flush()

    return tweets_list
