import json
import time
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

pages = ['home', 'about', 'contact', 'products', 'blog']
users = [f"user_{i}" for i in range(1, 101)]

print("Starting traffic event simulation...")
while True:
    event = {
        "user": random.choice(users),
        "page": random.choice(pages),
        "timestamp": time.time()
    }
    producer.send('web-traffic', value=event)
    time.sleep(0.05)
