from confluent_kafka import Producer
import socket


class KafkaProducer:
    def __init__(self):
        # TODO: Add optional parameters for acks, retries, etc. Look into SerializingProducer
        self.config = {'bootstrap.servers': "host1:9092,host2:9092",
                       'client.id': socket.gethostname()}
        self.producer = Producer(self.config)

    def send(self, topic_name, k, v):
        # TODO: Set up error handling if msg not delivered and flush()
        return self.producer.produce(topic=topic_name, key=k, value=v)
