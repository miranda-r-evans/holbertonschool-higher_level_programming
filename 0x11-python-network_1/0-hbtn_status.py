#!/usr/bin/python3
'''
fetches a webpage
'''

from urllib.request import urlopen


if __name__ == "__main__":
        with urlopen('https://intranet.hbtn.io/status') as response:
                message = response.read()
                print("Body response:")
                print('\t- type: {}'.format(message.__class__))
                print('\t- content: {}'.format(message))
                print('\t- utf8 content: {}'.format(message.decode('utf-8')))
