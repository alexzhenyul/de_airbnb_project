import pandas as pd
from kafka import KafkaProducer
from time import sleep
from json import dumps
import random
import json

producer = KafkaProducer(bootstrap_servers=['172.31.39.90:9092'],
                         value_serializer=lambda x: 
                         dumps(x).encode('utf-8'))

review_df = pd.read_csv("data/review.csv")

while True:
    review_dict = review_df.sample(1).to_dict(orient="records")[0]
    sleep_time = random.randrange(999)
    producer.send('review', value=review_dict)
    sleep(sleep_time)
    
    
# producer.flush() #clear data from kafka server