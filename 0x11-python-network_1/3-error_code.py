#!/usr/bin/python3
'''
fetches a webpage
'''

from urllib.request import urlopen
from urllib.error import HTTPError
from sys import argv


try:
        with urlopen(argv[1]) as response:
                print(response.read().decode('utf-8'))
except HTTPError as e:
        print('Error code:', e.code)
except Exception as e:
        raise(e)
