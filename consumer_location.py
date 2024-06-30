from kafka import KafkaConsumer, TopicPartition
import json
from pymongo import MongoClient
import logging

logging.warning('Starting location consumer')

# Kafka configuration
topic_name = 'location'
bootstrap_servers = ['kafka_b:9094']  
consumer = KafkaConsumer(
    topic_name,
    bootstrap_servers=bootstrap_servers,
    auto_offset_reset='earliest',
    auto_commit_interval_ms=500,
    enable_auto_commit=True,
    group_id='2',
    value_deserializer=lambda x: json.loads(x.decode('utf-8')), 
    fetch_min_bytes=1,  
    fetch_max_wait_ms=1000, 
    session_timeout_ms=10000
)
consumer.subscribe([topic_name])

logging.warning('Subscribed to topic: location')

# Pymongo configuration
client = MongoClient("mongodb://mongo:27017")

logging.warning('Initiated mongo client')

database = client.weather_data
collection = database.location

# Message consumption
logging.warning(f"Listening to topic: {topic_name}")
try:
    for message in consumer:
        collection.insert_one(message.value)
        logging.warning(message.value)
finally:
    consumer.commit()
    consumer.close()