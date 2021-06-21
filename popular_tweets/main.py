from topic import Topic
from producer import KafkaProducer
from consumer import KafkaConsumer
from twitter_client import TwitterClient
from pprint import pprint


def main():
    topic_name = "test"
    partitions = 3
    replication_factor = 3

    twitter_topic = Topic()
    twitter_topic.create_topic(topic_name, partitions, replication_factor)

    twitter_client = TwitterClient()
    api_results = twitter_client.search("conspiracy")
    parsed_results = twitter_client.parse_tweets(api_results)

    twitter_producer = KafkaProducer()

    map(lambda k, v: twitter_producer.send(topic_name, k=k, v=v), parsed_results.items())

    twitter_consumer = KafkaConsumer()
    twitter_consumer.subscribe(topic_name)
    twitter_consumer.poll()


if __name__ == "__main__":
    main()
