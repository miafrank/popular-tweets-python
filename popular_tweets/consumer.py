from confluent_kafka import Consumer
import socket


class KafkaConsumer:
    def __init__(self):
        self.config = {'bootstrap.servers': "localhost:9092",
                       'group.id': 'tandem-dev-dish',
                       'client.id': socket.gethostname()}
        self.consumer = Consumer(self.config)

    def subscribe(self, topic):
        return self.consumer.subscribe([topic])

    def poll(self):
        # TODO: check message that is returned - error messages are returned as None. Add timeout.
        print(self.consumer.poll(timeout=10))
