import os
import finnhub
from datetime import date, timedelta
import sqlite3
from pathlib import Path
from newspaper import Article
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("FINNHUB_KEY")


#This is to set up the client(idk what that really means)
finnhub_client = finnhub.Client(api_key=API_KEY)
news = finnhub_client.general_news('general', min_id=0)
print(type(news))
print(news[0].keys())

#This will be where we create the database
connection = sqlite3.connect("NewsArticles.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS articles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    article_id INTEGER,
    category TEXT, 
    datetime INTEGER,
    headline TEXT,
    related TEXT,
    source TEXT, 
    summary TEXT,
    full_text TEXT,
    url TEXT,
    inserted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
'''
)

cursor.execute("""
CREATE UNIQUE INDEX IF NOT EXISTS idx_articles_article_id
ON articles(article_id)
""")


#This just prints the stuff out
count = 1
for article in news:
    url = article['url']
    full_text = None
    try:
        specArticle = Article(url)
        specArticle.download()
        specArticle.parse()
        full_text = specArticle.text
    except Exception:
        full_text = None


    cursor.execute("INSERT OR IGNORE INTO articles (article_id, category, datetime, headline, related," \
    "source, summary, full_text, url) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
    (article['id'], article['category'],article['datetime'],
    article['headline'],article['related'],article['source'],
    article['summary'], full_text, article['url']))

    count +=1
connection.commit()

cursor.execute("SELECT COUNT(*) FROM articles")
print("Total rows in articles:", cursor.fetchone()[0])
