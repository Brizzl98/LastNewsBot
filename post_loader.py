import config
import requests
import feedparser
from datetime import timedelta, datetime
from dateutil import parser
from time import sleep
import ssl


class PostLoader:
    def __init__(self):
        self.__token = config.token
        self.__id = config.id
        self.feed_url = config.FEED_URL

    if hasattr(ssl, '_create_unverified_context'):
        ssl._create_default_https_context = ssl._create_unverified_context
		
    def send_message(self, message):
        requests.get(f'https://api.telegram.org/bot{self.__token}/sendMessage?chat_id={self.__id}&text={message}')


    def get_post(self):
        rss_feed = feedparser.parse(self.feed_url)
        entry=rss_feed.entries[0]
        self.send_message(entry.links[0].href)

if __name__ == "__main__":
    loader = PostLoader()
    loader.get_post()