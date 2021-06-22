from confluent_kafka import Producer
from logger import Logger
import socket
import json
from time import sleep


class KafkaProducer:
    def __init__(self):
        self.config = {'bootstrap.servers': "localhost:9092",
                       'client.id': socket.gethostname(),
                       'retries': 2}
        self.producer = Producer(self.config)
        self.logger = Logger(str(KafkaProducer.__class__))

    def send(self, topic_name, k: str, v: dict):
        try:
            self.producer.produce(topic=topic_name,
                                  key=k,
                                  value=json.dumps(v).encode('utf-8'),
                                  on_delivery=self.on_delivery)
        except BufferError:
            self.logger.error('%% Local producer queue is full (%d messages awaiting delivery): try again\n' %
                              len(self.producer))
        self.producer.poll(0)
        self.wait_and_flush()

    def on_delivery(self, err, msg):
        if err:
            self.logger.error(f"%% Message failed delivery: %s\n' % {err}")
        else:
            self.logger.info(('%% Message delivered to Producer %s [%d] @ %d\n' %
                              (msg.topic(), msg.partition(), msg.offset())))

    def wait_and_flush(self):
        sleep(5)
        self.logger.info('%% Waiting for %d deliveries\n' % len(self.producer))
        self.producer.flush()
