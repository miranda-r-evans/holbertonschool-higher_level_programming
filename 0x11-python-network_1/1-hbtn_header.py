#!/usr/bin/python3
'''
displays value of X-Request-Id variable from header of a response
'''

from urllib.request import urlopen
from sys import argv


with urlopen(argv[1]) as response:
        print(dict(response.getheaders())['X-Request-Id'])
