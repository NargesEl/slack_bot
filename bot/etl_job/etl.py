import pymongo
import time
from pymongo import collection
from sqlalchemy import create_engine
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

time.sleep(15)  # seconds
s  = SentimentIntensityAnalyzer()
pg = create_engine('postgresql://postgres:postgres@postgresdb:5432/tweets', echo=True)

pg.execute('''
    CREATE TABLE IF NOT EXISTS tweets (
    username VARCHAR(255),
    followers NUMERIC,
    timestamp VARCHAR(255),
    text VARCHAR(500),
    sentiment NUMERIC
);
''')

# Establish a connection to the MongoDB server
client = pymongo.MongoClient("mongodb")

# Select the database you want to use withing the MongoDB server
db = client.tweets
collection = db.tweets

entries = collection.find()


for e in entries:
    sentiment = s.polarity_scores(e['text'])  # assuming your JSON docs have a text field
    username = e['username']
    followers = e['followers_count']
    timestamp = e['timestamp']
    text = e['text']
    score = sentiment['compound']
    query = "INSERT INTO tweets VALUES (%s, %s, %s, %s, %s);"
    pg.execute(query, (username, followers, timestamp, text, score))
    print(e)
    print(sentiment)
#collection.to_sql('tweets', pg, if_exists='replace')
