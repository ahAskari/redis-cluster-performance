from rediscluster import RedisCluster
from nodes import startup_nodes

rc = RedisCluster(startup_nodes=startup_nodes, port=6379, password='1')


def get_keys(length: int):
    is_exist = False

    for i in range(0, length):
        is_exist = bool(rc.exists(str(i)))

        if is_exist == False:
            break
        else:
            continue

    if is_exist == False:
        print('key does not exist!')
    else:
        print('all keys retrieved')


