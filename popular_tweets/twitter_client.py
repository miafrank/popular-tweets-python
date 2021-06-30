import twitter
from popular_tweets import twitter_env


class TwitterClient:
    def __init__(self):
        self.creds = twitter_env.get_creds()
        self.api = twitter.Api(consumer_key=self.creds["twitter_consumer_key"],
                               consumer_secret=self.creds["twitter_consumer_secret"],
                               access_token_key=self.creds["twitter_access_key"],
                               access_token_secret=self.creds["twitter_access_secret"])

    def search(self, term):
        return self.api.GetSearch(term)

    @staticmethod
    def parse_tweets(search_results):
        results = {}
        for tweets in search_results:
            key = str(tweets.id)
            value = {'user': tweets.user.screen_name, 'tweet': tweets.text, 'favorite_count': tweets.favorite_count}
            results[key] = value
        return results
