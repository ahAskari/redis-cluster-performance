import random
import string


def gen_rand_chars(length: int = 20):
    chars: str = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))


def gen_dict(length: int) -> dict:
    obj: dict = {}
    for key in range(0, length):
        obj[key] = gen_rand_chars()
    return obj


def convert_mb_to_bytes(input: int):
    return input * 1024 * 1024


def convert_bytes_to_mg(input: int):
    return input / 1024 / 1024


def memory_usage_percentage(current: int, total: int):
    return float(current) / float(total) * 100


def print_result(arg1, arg2, arg3):
    print(f'current_memory: {convert_bytes_to_mg(arg1)} \n')
    print(f'memory_usage_percentage: {arg2}% \n')
    print(f'total: {convert_bytes_to_mg(arg3)} \n')
