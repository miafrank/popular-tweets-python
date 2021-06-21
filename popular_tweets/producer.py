from confluent_kafka import Producer
from confluent_kafka.error import ProduceError
from logger import Logger
import socket
import json


class KafkaProducer:
    def __init__(self):
        self.config = {'bootstrap.servers': "localhost:9092",
                       'client.id': socket.gethostname(),
                       'retries': 1}
        self.producer = Producer(self.config)
        self.logger = Logger(str(KafkaProducer.__class__))

    def send(self, topic_name, k: str, v: dict):
        self.producer.produce(topic=topic_name,
                              key=k,
                              value=json.dumps(v).encode('utf-8'),
                              on_delivery=self.on_delivery)
        self.producer.poll()

    def on_delivery(self, err, msg):
        if err:
            self.logger.error(f"%% Message failed delivery: %s\n' % {err}")
        else:
            self.producer.flush(timeout=5.0)
            self.logger.info(('%% Message delivered to %s [%d] @ %d\n' %
                              (msg.topic(), msg.partition(), msg.offset())))
