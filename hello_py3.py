/usr/bin/env python3

def greeting(name):
    return 'Hello, {}'.format(name)

def greeting(name: str) -> str:
    return 'Hello, {}'.format(name)
