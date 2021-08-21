# slack_bot

I built a ETL pipeline that collected tweets written by Ines Montani and stored them in a postgres database. I then analyzed the sentiment of the tweets and stored the annoted tweets in a second database on MongoDB. Finally, I connected it to my Slack and posted a tweet every few minutes. 

The config.py in the tweet_collector and in the slack_bot need to be filled in.These information can be found in your Twitter API in the Twitter developer account and your Slack API.

Tweets from a different account can be used by replacing the "id" in the tweet_collector.py and replacing the "image_url" in the slackbot.py.


<img width="818" alt="Screenshot 2021-08-21 at 13 30 51" src="https://user-images.githubusercontent.com/80095773/130320376-9e1391af-afa9-47ee-814b-b5e8bc6f7a08.png">
