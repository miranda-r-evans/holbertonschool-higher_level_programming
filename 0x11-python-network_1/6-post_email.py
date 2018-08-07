#!/usr/bin/python3
'''
fetches a webpage
'''

from requests import post
from sys import argv


if __name__ == "__main__":
        response = post(argv[1], data={'email': argv[2]})
        print(response.text)
