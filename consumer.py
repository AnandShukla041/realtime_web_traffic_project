from kafka import KafkaConsumer
import json
from collections import Counter
import threading

page_counter = Counter()
active_users = set()
lock = threading.Lock()

def consume_events():
    global page_counter, active_users
    consumer = KafkaConsumer(
        'web-traffic',
        bootstrap_servers='localhost:9092',
        value_deserializer=lambda m: json.loads(m.decode('utf-8'))
    )

    for message in consumer:
        event = message.value
        with lock:
            page_counter[event['page']] += 1
            active_users.add(event['user'])

threading.Thread(target=consume_events, daemon=True).start()

def get_metrics():
    global page_counter, active_users
    with lock:
        metrics = {
            "pages": dict(page_counter),
            "active_users": len(active_users)
        }
        page_counter.clear()
        active_users.clear()
    return metrics
