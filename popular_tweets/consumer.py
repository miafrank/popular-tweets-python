from confluent_kafka import Consumer
import socket
from logger import Logger


class KafkaConsumer:
    def __init__(self):
        self.config = {'bootstrap.servers': "localhost:9092",
                       'group.id': 'tandem-dev-dish',
                       'client.id': socket.gethostname()}
        self.consumer = Consumer(self.config)
        self.logger = Logger(str(KafkaConsumer.__class__))

    def subscribe(self, topic):
        return self.consumer.subscribe([topic], on_assign=self.on_assignment)

    def on_assignment(self, _, partitions):
        self.logger.info(f"Assignment: {partitions}")

    def poll(self):
        msgs = self.consumer.poll(timeout=20)
        self.logger.warn("Consumer timed out polling for msgs") if msgs is None else print(msgs.value(payload=msgs))
