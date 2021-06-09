import twitter
from popular_tweets import twitter_env


class TwitterClient:
    def __init__(self):
        self.creds = twitter_env.get_creds()
        self.api = twitter.Api(consumer_key=self.creds["twitter_consumer_key"],
                               consumer_secret=self.creds["twitter_consumer_secret"],
                               access_token_key=self.creds["twitter_access_key"],
                               access_token_secret=self.creds["twitter_access_secret"])
        return self.api

    def search(self, term):
        return self.api.GetSearch(term)
