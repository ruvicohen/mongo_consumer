import json
import os
from dotenv import load_dotenv
from kafka import KafkaConsumer
from app.repository.event_repository import insert_events
from app.service.event_service import convert_to_mongo_compatible
from app.service.validation_service import validate_event

load_dotenv(verbose=True)

bootstrap_servers = os.environ["BOOTSTRAP_SERVERS"]


def consume_topic(topic, process_message):
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers=bootstrap_servers,
        value_deserializer=lambda x: json.loads(x.decode("utf-8")),
    )
    for message in consumer:
        for event in message.value:
            event = convert_to_mongo_compatible(event)
            event = validate_event(event)

            if event:
                insert_events(event)
                print("Validated Event: ")
            else:
                print("Event validation failed.")
