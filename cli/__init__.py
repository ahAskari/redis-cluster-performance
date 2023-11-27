import argparse


def cli_handler():
    parser = argparse.ArgumentParser(
        prog='time to leave', usage='get time to leave')
    parser.add_argument('--num_keys', '-n', type=int, required=True)
    parser.add_argument('--expire', '-e', type=int)
    parser.add_argument('--memory', '-m', type=int)
    parser.add_argument('--type', '-t', choices=['get', 'set'], default='set')
    args = parser.parse_args()
    return args
