import feedparser
import json

url = ''
feed = feedparser.parse('https://www.reuters.com/')

print(feed.keys())

for article in feed:
    print(f"\nHeadline: {feed['headers']}")
