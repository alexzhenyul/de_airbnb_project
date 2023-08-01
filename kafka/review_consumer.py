from kafka import KafkaConsumer
from time import sleep
from json import dumps,loads
import json
from s3fs import S3FileSystem

consumer = KafkaConsumer(
    'review',
     bootstrap_servers=['172.31.39.90:9092'], #add your IP here
    value_deserializer=lambda x: loads(x.decode('utf-8')))

s3 = S3FileSystem()

for count, i in enumerate(consumer):
    with s3.open("s3://raw-bucket-alexl/review_{}.json".format(count), 'w') as file:
        json.dump(i.value, file)   
    