import os
from app.kafka_settings.consumer import consume_topic
from dotenv import load_dotenv

load_dotenv(verbose=True)

mongo_topic = os.environ["MONGO_TOPIC"]

if __name__ == "__main__":
    consume_topic(mongo_topic, print)
