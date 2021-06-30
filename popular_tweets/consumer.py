from confluent_kafka import Consumer, KafkaException
import socket
from logger import Logger


class KafkaConsumer:
    def __init__(self):
        self.config = {'bootstrap.servers': "localhost:9092",
                       'group.id': 'tandem-dev-dish',
                       'client.id': socket.gethostname(),
                       'session.timeout.ms': 6000,
                       'auto.offset.reset': 'earliest'}
        self.logger = Logger(str(KafkaConsumer.__class__))
        self.consumer = Consumer(self.config)

    def subscribe(self, topic):
        return self.consumer.subscribe([topic], on_assign=self.on_assignment)

    def on_assignment(self, _, partitions):
        self.logger.info(f"Assignment: {partitions}")

    def poll(self):
        try:
            while True:
                msg = self.consumer.poll(timeout=10)
                if msg is None:
                    self.logger.error("Consumer timed out")
                    return
                if msg.error():
                    raise KafkaException(msg.error())
                else:
                    self.logger.info('%% %s [%d] at offset %d with key %s:\n' %
                                     (msg.topic(), msg.partition(), msg.offset(),
                                      str(msg.key())))

        except KeyboardInterrupt:
            self.logger.error('%% Aborted by user\n')

        finally:
            self.consumer.close()
