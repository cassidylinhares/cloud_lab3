from confluent_kafka import Consumer
import json
import time
import io
from avro.io import DatumReader, BinaryDecoder
import avro.schema

schema = avro.schema.parse(open("./schema.avsc").read())
reader = DatumReader(schema)

def decode(msg_value):
    message_bytes = io.BytesIO(msg_value)
    message_bytes.seek(5)
    decoder = BinaryDecoder(message_bytes)
    event_dict = reader.read(decoder)
    return event_dict 

consumer = Consumer({
    'bootstrap.servers': 'pkc-3w22w.us-central1.gcp.confluent.cloud:9092',
    'group.id': 'boop',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': 'N6X6STEHV7XVBGBC',
    'sasl.password': 'A9gGbpJ1DbzpJ/iTAYDAzl3Os+K2hQXNbTEecxohpOP9bQw3rAunZHESgoDKnVHa',
    'session.timeout.ms': 45000,
    'auto.offset.reset': 'earliest'
})

# Subscribe to topic
consumer.subscribe(['myDBtest'])

print("Consumer subscribed")

# Process messages
while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        print("Consumer error: {}".format(msg.error()))
        continue

    decoded_msg = decode(msg.value())
    print('Received message: {} on Partition: {}'.format(
        decoded_msg, msg.partition()))


consumer.close()
