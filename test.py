#This is the file that is for me to test and learn new conce=epts as I icorporate them
#into my code
import os
import finnhub
import json
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("FINNHUB_KEY")


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
