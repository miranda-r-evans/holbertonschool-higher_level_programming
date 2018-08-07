#!/usr/bin/python3
'''
fetches a webpage
'''

from requests import get


if __name__ == "__main__":
        response = get('https://intranet.hbtn.io/status')
        response = response.content.decode('utf-8')
        print("Body response:")
        print('\t- type:', response.__class__)
        print('\t- content:', response)
