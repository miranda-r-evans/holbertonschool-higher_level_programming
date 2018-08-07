#!/usr/bin/python3
'''
sends POST request to a url, using email variable
'''

from urllib.request import urlopen, Request
from urllib.parse import urlencode
from sys import argv


if __name__ == "__main__":
        data = {'email': argv[2]}
        data = urlencode(data)
        data = data.encode('utf-8')
        req = Request(url=argv[1], data=data, method='POST')
        with urlopen(req) as response:
                print(response.read().decode('utf-8'))
