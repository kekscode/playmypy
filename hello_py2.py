/usr/bin/env python2

def greeting(name):
    return 'Hello, {}'.format(name)

def greeting(name): # type: str -> str
    return 'Hello, {}'.format(name)
