# TODO: setup script to create topic and run producer and consumer
from pprint import pprint

from topic import Topic
from producer import KafkaProducer
from consumer import KafkaConsumer
from twitter_client import TwitterClient


def main():
    topic_name = "test"
    partitions = 1
    replication_factor = 3

    twitter_topic = Topic()
    twitter_topic.create_topic(topic_name, partitions, replication_factor)

    twitter_client = TwitterClient()
    api_results = twitter_client.search("conspiracy")
    parsed_results = twitter_client.parse_tweets(api_results)

    # Status(ID=1405018801922613248, ScreenName=funder, Created=Wed  2021, Text = 'The trump White House pressured
    # the DoJ to join their conspiracy to overturn the election. Clearly the worst abuse… https://t.co/q8RgSY0tD4'

    twitter_producer = KafkaProducer()
    # TODO: send twitter msgs to producer
    map(lambda k, v: twitter_producer.send(topic_name, k=k, v=v), parsed_results.items())

    # Create consumer and print/list tweets
    pass


if __name__ == "__main__":
    main()
