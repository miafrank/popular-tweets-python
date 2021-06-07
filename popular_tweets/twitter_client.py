import twitter
from popular_tweets import twitter_env

def client():
  creds = twitter_env.get_creds()
  api = twitter.Api(consumer_key=creds["twitter_consumer_key"],
                    consumer_secret=creds["twitter_consumer_secret"],
                    access_token_key=creds["twitter_access_key"],
                    access_token_secret=creds["twitter_access_secret"])
  return api