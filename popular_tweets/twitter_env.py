import os

def get_creds():
  creds = twitter_credentials()
  
  if all(creds.values()): 
     return creds
  else:
    return("All required env variables are not provided")

def twitter_credentials(): 
  return {
    "twitter_consumer_key":  os.environ.get("TWITTER_CONSUMER_KEY"),
    "twitter_consumer_secret":  os.environ.get("TWITTER_CONSUMER_SECRET"),
    "twitter_access_key": os.environ.get("TWITTER_ACCESS_KEY"),
    "twitter_access_secret": os.environ.get("TWITTER_ACCESS_SECRET")
  }