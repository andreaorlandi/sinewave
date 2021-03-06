import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)

pubsub = r.pubsub()
pubsub.subscribe('sinewave')

for item in pubsub.listen():
    if item['type'] == 'message':
        print(item['data'])
