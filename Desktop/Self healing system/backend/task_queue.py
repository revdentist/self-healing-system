import json
import redis

r = redis.Redis(host="localhost", port=6379, db=0)

QUEUE_KEY = "log_queue"

def enqueue_log(log_dict: dict):
    r.lpush(QUEUE_KEY, json.dumps(log_dict))

def dequeue_log():
    data = r.rpop(QUEUE_KEY)
    if data:
        return json.loads(data)
    return None
