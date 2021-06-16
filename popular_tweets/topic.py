from confluent_kafka.admin import AdminClient, NewTopic, KafkaException
from logger import Logger
import socket


class Topic:
    def __init__(self):
        self.admin_client = AdminClient({'bootstrap.servers': "localhost:9092",
                                         'client.id': socket.gethostname()})
        self.logger = Logger(str(Topic.__class__))

    def create_topic(self, topic_name, partitions, replication_factor):
        topic = NewTopic(topic_name, partitions, replication_factor)
        try:
            client_topic, = self.admin_client.create_topics([topic])
            self.logger.info(f"Successfully created topic {client_topic}")
        except KafkaException as k:
            self.logger.info(f"Error:{k}. Failed to create topic {topic_name}")
