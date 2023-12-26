import redis

redis_connection = redis.Redis(
    host='redis',
    port=6379,
    db=1,
    charset='utf-8',
    decode_responses=True
)
