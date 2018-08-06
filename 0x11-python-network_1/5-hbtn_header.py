#!/usr/bin/python3
'''
fetches a webpage
'''

from requests import get
from sys import argv


response = get(argv[1])
print(response.headers['X-Request-Id'])
