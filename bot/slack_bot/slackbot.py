#import random
import requests
import config
from sqlalchemy import create_engine
import pandas as pd
import time

time.sleep(15)
counter = 0

while True:
    
    engine = create_engine( config.p_config, echo=True)
    webhook_url = config.webhook_url
    selection = pd.read_sql(f'SELECT * FROM tweets ORDER BY timestamp ASC offset {counter} limit 1;', engine)
    requests.post(url=webhook_url, json = {'blocks': [{
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"{selection['username']}*tweeted:\n{selection['text']}*at*{selection['timestamp']}\n*The Tweet has a Vader Sentiment Value of:* {selection['sentiment']}\n"
                },
                "accessory": {
                    "type": "image",
                    "image_url": "https://avatars.githubusercontent.com/u/13643239?v=4",
                    "alt_text": "Ines Monatni"
                }
            }]
    })
    counter = counter + 1
    time.sleep(15)
