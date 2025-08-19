import finnhub
import json


API_KEY = 'd1himi1r01qsvr2ae0mgd1himi1r01qsvr2ae0n0'
finnhub_client = finnhub.Client(api_key=API_KEY)

news = finnhub_client.general_news('general', min_id=0)
count = 1
for article in news:
    print(f"\n------Article #{count}---- ")
    print(f"Headline: {article['headline']}")
    print(f"Category: {article['category']}")
    print(f"Summary: {article['summary']}")
    print(f"URL: {article['url']}")
    count +=1
