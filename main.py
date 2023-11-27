from set_keys import set_keys
from cli import cli_handler
from get_keys import get_keys

if __name__ == '__main__':
    arg = cli_handler()

    if arg.type == 'get':
        get_keys(arg.num_keys)
    elif arg.type == 'set':
        set_keys(arg.num_keys, arg.expire, arg.memory)
