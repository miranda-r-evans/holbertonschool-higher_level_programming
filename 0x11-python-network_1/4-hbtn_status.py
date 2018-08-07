#!/usr/bin/python3
'''
fetches a webpage
'''

from requests import get


if __name__ == "__main__":
        response = get('https://intranet.hbtn.io/status')
        print("Body response:")
        print('\t - type:', response.reason.__class__)
        print('\t - content:', response.reason)
