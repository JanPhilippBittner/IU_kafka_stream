from kafka import KafkaProducer
import json
import time
import requests
import datetime
import logging

# API URI
api_url = 'https://api.openweathermap.org/data/2.5/weather?lat=45.13&lon=7.61&appid=<your API key>'
# Topic specification
topic_1 = 'weather'
topic_2 = 'location'


logging.warning('Starting producer')
# Producer creation
producer = KafkaProducer(bootstrap_servers='kafka_b:9094'  , value_serializer=lambda v: json.dumps(v).encode('utf-8'))
logging.warning('Connected to Kafka')


try:
    while True:
        # API request
        request = requests.get(api_url)
        data_dic = request.json()

        # Data parsing and cleaning
        unique_identifier = str(data_dic['dt']) + data_dic['name'].replace(' ','')
        timestamp = datetime.datetime.fromtimestamp(data_dic['dt'] , datetime.timezone.utc)
        location = {'loc_tim_id' : unique_identifier , 'name' : data_dic['name'], 'coordinates': data_dic['coord'], 'time':str(timestamp)}
        weather = {'loc_tim_id' : unique_identifier , 'weather' : data_dic['weather'] , 'wind' : data_dic['wind'] , 'measurements': data_dic['main']} 

        # Producer sending data to Kafka
        producer.send(topic=topic_1 , value=weather)
        logging.warning(f'Send message to {topic_1}. Sleeping....')
        producer.send(topic=topic_2 , value=location)
        logging.warning(f'Send message to {topic_2}. Sleeping....')
        time.sleep(3)
        producer.flush()
finally:
    # Closing Kafka properly
    producer.close()
    logging.warning('Producer closed.')