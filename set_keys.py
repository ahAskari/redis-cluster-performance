import random
import string
from rediscluster import RedisCluster
from nodes import startup_nodes
from utils import convert_mb_to_bytes, memory_usage_percentage, print_result

rc = RedisCluster(startup_nodes=startup_nodes, port=6379,
                  password='1', decode_responses=True)

threshold = 60


def set_keys(length: int, expire: int, given_memory: int):
    rc.flushall()
    rc.flushdb()

    for i in range(0, length):
        value = ''.join(random.choices(
            string.ascii_letters + string.digits, k=1000000))
        rc.set(str(i), value, ex=expire)

        current = current_memory()
        total = total_memory()
        # total = convert_mb_to_bytes(given_memory)
        current_usage_percentage = memory_usage_percentage(current, total)

        print_result(current, current_usage_percentage, total)

        if current_usage_percentage >= threshold:
            print("Memory usage exceeded the defined limit")
            print(f'The number of stored keys: {i+1}')
            break
        else:
            continue


def current_memory():
    info = rc.info('memory')
    return info['10.200.200.2:6379']['used_memory']


def total_memory():
    info = rc.info('memory')
    return info['10.200.200.2:6379']['total_system_memory']
