from confluent_kafka import Producer
from avro.io import DatumWriter, BinaryEncoder
import avro.schema
import json;
import time
import io;

schema = avro.schema.parse(open("./schema.avsc").read())
writer = DatumWriter(schema)
schemaID=100001;

producer = Producer({
    'bootstrap.servers': 'pkc-3w22w.us-central1.gcp.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': 'N6X6STEHV7XVBGBC',
    'sasl.password': 'A9gGbpJ1DbzpJ/iTAYDAzl3Os+K2hQXNbTEecxohpOP9bQw3rAunZHESgoDKnVHa',
    'session.timeout.ms': 45000,
})

print("Connected!")


def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(
            msg.topic(), msg.partition()))


def encode(value):
    bytes_writer = io.BytesIO()
    encoder = BinaryEncoder(bytes_writer)
    writer.write(value, encoder)
    return schemaID.to_bytes(5, 'big')+bytes_writer.getvalue()

value={'id':15,'name':"user",'email':'test@gmail.com','department':"IT",'modified':int(1000*time.time())};
encoded_val = encode(value)


producer.poll(0)
producer.produce('ToMySQL', value=encoded_val, callback=delivery_report)

print("Sending: {} {}".format(value['id'], value['name']))

producer.flush()
