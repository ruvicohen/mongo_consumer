import json
import os
from dotenv import load_dotenv
from kafka import KafkaConsumer

load_dotenv(verbose=True)

bootstrap_servers = os.environ["BOOTSTRAP_SERVERS"]

def consume_topic(topic, process_message):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
    for message in consumer:
        print(message)
        for tweet_data in message.value:
            process_message(tweet_data)