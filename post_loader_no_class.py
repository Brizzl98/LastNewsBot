import config
import requests
import feedparser
from datetime import timedelta, datetime
from dateutil import parser
from time import sleep
import ssl

token = config.token
id = config.id


def send_message(message):
	requests.get(f'https://api.telegram.org/bot{token}/sendMessage?chat_id={id}&text={message}')


if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context
	
FEED_URL = 'https://vc.ru/rss/new'

def get_post():
    rss_feed = feedparser.parse(FEED_URL)
    entry=rss_feed.entries[0]
    send_message(entry.links[0].href)


if __name__ == "__main__":
	get_post()