#!/usr/bin/python3
'''
fetches a webpage
'''

from requests import get
from sys import argv

response = get(argv[1])
if response.status_code >= 400:
        print('Error code:', response.status_code)
else:
        print(response.text)
