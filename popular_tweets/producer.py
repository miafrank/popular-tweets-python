from confluent_kafka import Producer
from confluent_kafka.error import ProduceError
from logger import Logger
import socket
import json


class KafkaProducer:
    def __init__(self):
        # TODO: Add optional parameters for acks, retries, etc. Look into SerializingProducer
        self.config = {'bootstrap.servers': "localhost:9092",
                       'client.id': socket.gethostname()}
        self.producer = Producer(self.config)
        self.logger = Logger(str(KafkaProducer.__class__))

    def send(self, topic_name, k: str, v: dict):
        # TODO Add logs when msg sent successfully
        return self.producer.produce(topic=topic_name,
                                     key=k,
                                     value=json.dumps(v).encode('utf-8'),
                                     on_delivery=self.on_delivery())

    def on_delivery(self):
        try:
            self.producer.flush(timeout=5.0)
        except ProduceError as k:
            self.logger.warn(f"Error: {k.exception} Producer failed on timeout when polling")
